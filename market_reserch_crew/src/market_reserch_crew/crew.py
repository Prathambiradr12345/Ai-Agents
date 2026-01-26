"""from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool,ScrapeWebsiteTool,SeleniumScrapingTool
from dotenv import load_dotenv

load_dotenv()

#for Tool
web_serch_tool=SerperDevTool()
Web_Scrape_tool=ScrapeWebsiteTool()
selenium_scraping_tool=SeleniumScrapingTool()


toolkit=[web_serch_tool,Web_Scrape_tool,selenium_scraping_tool]
#define the crew class
@CrewBase
class MarketReserchCrew():
    #MarketReserchCrew crew

    agents: List[BaseAgent]
    tasks: List[Task]
     
     #provide the path
    agents_config="config/agents.yaml"
    tasks_config="config/tasks.yaml"
    
    #agents
    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["market_research_specialist"],
            tools=toolkit
        )
    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitive_intelligence_analyst"],
            tools=toolkit
        )    
    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["customer_insights_researcher"],
            tools=toolkit
        )    
    @agent    
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["product_strategy_advisor"],
            tools=toolkit
        )            
    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["business_analyst"],
            tools=toolkit
        )
    from crewai import Agent
    from crewai.llm import LLM
    from dotenv import load_dotenv
    load_dotenv()


    def market_research_specialist():
        llm = LLM(
        model="llama3-70b-8192",
        provider="groq"   # 🔥 FORCE GROQ
    )
        return Agent(
        role="Market Research Specialist",
        goal="Analyze market trends and competitors",
        backstory="Expert in market intelligence",
        llm=llm,
        verbose=True
    )
        
    

    
   

    @task    
    def market_research_task(self) -> task:
        return task(
            config=self.tasks_config["market_research_task"]
        )
    @task    
    def competitive_intelligence_task(self) -> task:
        return task(
            config=self.tasks_config["competitive_intelligence_task"],
            context=[self.market_research_task()]
        )
    @task    
    def customer_insights_task(self) -> task:
        return task(
            config=self.tasks_config["customer_insights_task"],
            context=[self.market_research_task(),
                    self.competitive_intelligence_task]
        )  
    @task    
    def product_strategy_task(self) -> task:
        return task(
            config=self.tasks_config["product_strategy_task"],
            context=[self.market_research_task(),
                    self.competitive_intelligence_task(),
                    self.competitive_intelligence_task]
        )     
    @task    
    def business_analyst_task(self) -> task:
        return task(
            config=self.tasks_config["business_analyst_task"],
            context=[self.market_research_task(),
                    self.competitive_intelligence_task(),
                    self.competitive_intelligence_task(),
                    self.product_strategy_task]
        )
 
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            Process=Process.sequntial
        )"""
        
from crewai import Agent
from crewai.llm import LLM

class MarketReserchCrew:
    def market_research_specialist(self):
        groq_llm = LLM(
            model="llama3-70b-8192",
            provider="groq"
        )

        return Agent(
            role="Market Research Specialist",
            goal="Analyze market trends and competitors",
            backstory="Expert in market intelligence",
            llm="groq/llama3-70b-8192",
            verbose=True
        )

    def crew(self):
        return self.market_research_specialist()
        
from crewai import Agent

class MarketReserchCrew:
    def market_research_specialist(self):
        return Agent(
            role="Market Research Specialist",
            goal="Analyze market trends and competitors",
            backstory="Expert in market intelligence",
            llm="groq/llama3-70b-8192",
            verbose=True
        )

    def crew(self):
        return self.market_research_specialist()
from crewai import Agent, Task, Crew

class MarketReserchCrew:
    def market_research_specialist(self):
        return Agent(
            role="Market Research Specialist",
            goal="Analyze market trends",
            backstory="Expert in market analysis",
            llm="groq/llama-3.1-8b-instant",
            verbose=True
        )

    def crew(self):
        agent = self.market_research_specialist()

        task = Task(
            description="Analyze current AI market trends in India",
            expected_output="A short, clear summary of AI market trends",
            agent=agent
        )

        return Crew(
            agents=[agent],
            tasks=[task],
            verbose=True
        )


