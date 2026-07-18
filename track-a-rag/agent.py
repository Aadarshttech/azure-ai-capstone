"""
Track A - RAG-Based Q&A Agent
-------------------------------
This starter shows how to:
  1. Upload your documents to Foundry Agent Service (File Search tool)
  2. Create an agent that grounds answers in those documents
  3. Run a conversation and print responses with source citations

Prerequisites:
  - Azure AI Foundry project set up
  - PROJECT_CONNECTION_STRING in your .env file
  - Documents placed in the /data folder
"""

import os
from pathlib import Path
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FileSearchTool, ToolSet
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()


def upload_documents(client: AIProjectClient, data_dir: str) -> list[str]:
    """Upload all files in data_dir and return their file IDs."""
    file_ids = []
    data_path = Path(data_dir)

    if not data_path.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    for file_path in data_path.iterdir():
        if file_path.suffix.lower() in [".pdf", ".txt", ".md", ".docx"]:
            print(f"Uploading: {file_path.name}")
            with open(file_path, "rb") as f:
                uploaded = client.agents.upload_file_and_poll(
                    file=f,
                    purpose="assistants"
                )
            file_ids.append(uploaded.id)
            print(f"  -> File ID: {uploaded.id}")

    return file_ids


def create_rag_agent(client: AIProjectClient, file_ids: list[str]):
    """Create a Foundry agent with File Search attached."""
    file_search = FileSearchTool(file_ids=file_ids)
    tool_set = ToolSet(file_search=file_search)

    agent = client.agents.create_agent(
        model="gpt-4o",
        name="rag-qa-agent",
        instructions=(
            "You are a helpful assistant that answers questions strictly based on "
            "the uploaded documents. Always cite which document your answer comes from. "
            "If the answer is not in the documents, say so clearly."
        ),
        tools=tool_set.definitions,
        tool_resources=tool_set.resources,
    )
    print(f"Agent created: {agent.id}")
    return agent


def ask_question(client: AIProjectClient, agent, question: str) -> str:
    """Send a question to the agent and return the response with citations."""
    thread = client.agents.create_thread()

    client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content=question,
    )

    run = client.agents.create_and_process_run(
        thread_id=thread.id,
        agent_id=agent.id,
    )

    if run.status == "failed":
        return f"Run failed: {run.last_error}"

    messages = client.agents.list_messages(thread_id=thread.id)
    response = messages.data[0]  # Most recent message

    # Extract text and any file citations
    answer = ""
    for block in response.content:
        if hasattr(block, "text"):
            answer += block.text.value
            # Print inline citations if present
            if hasattr(block.text, "annotations") and block.text.annotations:
                print("\n[Sources cited]")
                for ann in block.text.annotations:
                    if hasattr(ann, "file_citation"):
                        print(f"  - File ID: {ann.file_citation.file_id}")

    return answer


def cleanup(client: AIProjectClient, agent, file_ids: list[str]):
    """Delete the agent and uploaded files."""
    client.agents.delete_agent(agent.id)
    for fid in file_ids:
        client.agents.delete_file(fid)
    print("Cleanup done.")


def main():
    client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=os.environ["PROJECT_CONNECTION_STRING"],
    )

    # Step 1 - Upload your documents from the /data folder
    file_ids = upload_documents(client, data_dir="data")

    if not file_ids:
        print("No supported files found in /data. Add .pdf, .txt, .md, or .docx files.")
        return

    # Step 2 - Create the agent
    agent = create_rag_agent(client, file_ids)

    # Step 3 - Ask questions in a loop
    print("\nRAG Q&A Agent ready. Type 'quit' to exit.\n")
    try:
        while True:
            question = input("Your question: ").strip()
            if question.lower() in ["quit", "exit", "q"]:
                break
            if not question:
                continue
            answer = ask_question(client, agent, question)
            print(f"\nAnswer:\n{answer}\n")
    finally:
        cleanup(client, agent, file_ids)


if __name__ == "__main__":
    main()
