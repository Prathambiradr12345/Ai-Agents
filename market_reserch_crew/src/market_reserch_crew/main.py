#!/usr/bin/env python
"""import sys
import warnings

from datetime import datetime

from market_reserch_crew.crew import MarketReserchCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    
    #Run the crew.
    
    inputs = {
          "product_idea": "An AI powered tool that summarizes youtube videos on my channel and posts the summary on various social media platforms like LinkedIn, Instagram, Facebook,X, WhatsApp"
    }

    try:
        MarketReserchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    
    #Train the crew for a given number of iterations.
    
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        MarketReserchCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    
    #Replay the crew execution from a specific task.
    
    try:
        MarketReserchCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
   
    #Test the crew execution and returns the results.
    
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        MarketReserchCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    
    #Run the crew with trigger payload.
   
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = MarketReserchCrew().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")"""
        
from dotenv import load_dotenv
load_dotenv()

from market_reserch_crew.crew import MarketReserchCrew

def run():
    print(" Starting Crew...")
    result = MarketReserchCrew().crew().kickoff()
    print(" Crew finished")
    print("RESULT:")
    print(result)

if __name__ == "__main__":
    run()
import os
os.environ["LITELLM_LOG"] = "ERROR"
os.environ["LITELLM_DISABLE_LOGGING"] = "true"
os.environ["LITELLM_DISABLE_PROXY"] = "true"
    
    
from dotenv import load_dotenv
load_dotenv()

from market_reserch_crew.crew import MarketReserchCrew

def run():
    #Run the crew.
    print("Starting Crew...")
    result = MarketReserchCrew().crew().kickoff()
    print(" Crew finished")
    print("\nRESULT:\n")
    print(result)

if __name__ == "__main__":
    run()
    

    

