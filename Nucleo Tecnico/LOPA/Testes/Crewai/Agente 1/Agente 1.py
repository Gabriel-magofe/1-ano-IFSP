import os
from crewai import Agent, Task, Crew, LLM

os.environ["GEMINI_API_KEY"] = "AQ.Ab8RN6LBIMgfFDVhUBziBH_UFLiM1hqd1y9NqceieyX12_8UEQ"
modelo_gemini = LLM(model="gemini/gemini-2.5-flash")
pesquisador = Agent(
    role="Pesquisador de Tecnologia",
    goal="Encontrar as 3 principais tendências de Inteligência Artificial para este ano.",
    backstory="Você é um jornalista de tecnologia focado em dados e novidades de IA.",
    llm=modelo_gemini
)
escritor = Agent(
    role="Redator de Conteúdo",
    goal="Pegar as tendências encontradas pelo pesquisador e criar um post curto para o LinkedIn.",
    backstory="Você é um especialista em marketing digital que escreve posts engajadores.",
    llm=modelo_gemini
)
tarefa_pesquisa = Task(
    description=(
        "Com base no seu conhecimento atual"
        "liste as 3 maiores novidades e tendências sobre Inteligência Artificial para este ano. "
        "Não tente buscar na internet, use seu conhecimento prévio."
    ),
    expected_output="Uma lista em tópicos com as 3 tendências.",
    agent=pesquisador
)

tarefa_escrita = Task(
    description="Com base na lista em tópicos gerada pelo pesquisador, escreva um post profissional e engajador para o LinkedIn.",
    expected_output="Um texto formatado para o LinkedIn com hashtags.",
    agent=escritor
)
equipe = Crew(
    agents=[pesquisador, escritor],
    tasks=[tarefa_pesquisa, tarefa_escrita],
    verbose=True
)
resultado_final = equipe.kickoff()

print("\n--- RESULTADO FINAL DO AGENTE ---")
print(resultado_final)
