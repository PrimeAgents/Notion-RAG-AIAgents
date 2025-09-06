from notion_client import Client
import os
from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

id=os.getenv("id")
api_key= os.getenv("api_key_gemini_v2")




notion = Client(auth=os.getenv("NOTION_TOKEN"))
def return_knowledge_base(agent, query, num_documents=None, **kwargs):
    database_id = "your_database_id_here"  # Replace with your Notion database ID

    try:
        results = notion.databases.query(database_id=database_id)
        matching_documents = []
        query_words = set(query.lower().split())

        for page in results['results']:
            page_props = page['properties']

            # Extract Q1/A1
            q1_data = page_props.get('Questions1', {}).get('title', [])
            a1_data = page_props.get('Answer1', {}).get('rich_text', [])

            question1 = q1_data[0]['plain_text'] if q1_data else ""
            answer1 = a1_data[0]['plain_text'] if a1_data else ""

            # Extract Q2/A2
            q2_data = page_props.get('Question2', {}).get('rich_text', [])
            a2_data = page_props.get('Answer2', {}).get('rich_text', [])

            question2 = q2_data[0]['plain_text'] if q2_data else ""
            answer2 = a2_data[0]['plain_text'] if a2_data else ""

            # Add Q1/A1 if valid
            if question1 and answer1:
                match_score = _compute_match_score(query_words, question1, answer1)
                matching_documents.append({
                    "content": f"Q: {question1}\nA: {answer1}",
                    "meta_data": {
                        "source": "Notion KB",
                        "match_score": match_score
                    }
                })

            # Add Q2/A2 if valid
            if question2 and answer2:
                match_score = _compute_match_score(query_words, question2, answer2)
                matching_documents.append({
                    "content": f"Q: {question2}\nA: {answer2}",
                    "meta_data": {
                        "source": "Notion KB",
                        "match_score": match_score
                    }
                })

        # Sort by match score descending
        matching_documents.sort(key=lambda doc: doc['meta_data']['match_score'], reverse=True)

        if matching_documents:
            print(f"✅ Found {len(matching_documents)} matching Q&A pairs")
            return matching_documents[:num_documents] if num_documents else matching_documents
        else:
            return [{
                "content": "No matching entry found in the knowledge base.",
                "meta_data": {"source": "Notion KB"}
            }]

    except Exception as e:
        print(f"❌ Error accessing Notion: {e}")
        return [{"content": f"Error: {str(e)}", "meta_data": {"source": "Error"}}]

# Helper function to compute keyword match
def _compute_match_score(query_words, question, answer):
    text_words = set((question + " " + answer).lower().split())
    matches = len(query_words.intersection(text_words))
    return matches / len(query_words) if query_words else 0

# Set up agent
agent = Agent(
    model=Gemini(id=id,api_key= api_key),
    knowledge=None,
    search_knowledge=True,
    retriever=return_knowledge_base,
    show_tool_calls=True,
)

# Test
prompt = input("Enter Your Prompt: ")
agent.print_response(prompt)

