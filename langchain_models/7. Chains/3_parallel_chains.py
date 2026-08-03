import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()

# Model 1
huggingface_llm1 = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B", task="text-generation"
)

model1 = ChatHuggingFace(llm=huggingface_llm1)

# Model 2
huggingface_llm2 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation"
)


model2 = ChatHuggingFace(llm=huggingface_llm2)


prompt1 = PromptTemplate(
    template="Generate the short and simple notes from the following text \n {text}",
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template="Generate 5 Question and Answers from the following text\n {text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and Quiz into a single document \n {notes} and {quiz}",
    input_variables=["notes", "quiz"],
)

parser = StrOutputParser()


parallel_Chain = RunnableParallel(
    {"notes": prompt1 | model1 | parser, "quiz": prompt2 | model2 | parser}
)


merge_chain = prompt3 | model1 | parser

final_chain = parallel_Chain | merge_chain


text = """
EU AI Act Article 50: What I Would Put in the Day-One Checklist

If a leadership team told me it was ready for Article 50, I would not begin with its AI policy󠇟󠇠󠇡󠇢󠅬󠄆︉󠅯󠄃󠄧󠆸󠇩󠇎󠄺󠅚󠄃󠄭󠆭󠇨󠆑󠄶󠆢󠄔󠇥󠅆󠆃󠄆󠅶︃󠅭󠄌󠅊󠅐󠅌󠇟󠇣󠄧︋󠄫󠆾󠅩󠄊󠆱󠄮. I would ask for one current system record and follow a marked output from generation to the place where an EU user actually receives it.󠇟󠇠󠇡󠇢󠆰󠅸︃󠄤󠄛󠄠󠅶󠅶󠅯󠅅󠆈󠇁︃󠄈󠇀󠅧󠆱󠄳󠇦󠇄󠇕󠆣󠅒󠆥︃󠄾󠇛󠆄︉󠆛󠅬󠆭󠇢󠅢󠇉󠆥󠅠󠆯󠅆󠆮

That short exercise exposes most of the gap between a written control and a working one.󠇟󠇠󠇡󠇢󠆍󠅫󠇃󠅤󠇛󠆶󠄜󠇭󠄱󠅟󠄥󠆖󠅲󠅃󠄩︋󠅋󠄧󠅯󠅪󠇜󠄣󠅷󠅳󠄱󠅉󠆞󠄮︄󠇑󠄅󠆵󠆄󠅰󠅭󠇂󠄱󠆡󠇠󠅇

Article 50's transparency obligations apply from August 2nd, 2026󠇟󠇠󠇡󠇢󠄯󠅟󠅿󠇌󠅊󠇪󠆉󠄚󠄘︋󠇛󠅬󠇪️󠆽︊󠇀︇󠄗󠇌󠄠󠆝󠅄󠆀󠆞󠆃︂󠅚󠄉󠄩︄󠄷󠅧󠇍󠇢󠅗󠇙󠇁󠆧󠅕. For organizations that generate or publish synthetic content, readiness turns on two different questions:

1󠇟󠇠󠇡󠇢󠅤󠅓󠆆󠆪󠇯󠄋󠅈󠇄󠇚󠆭󠅕󠅬󠅋󠆚󠇓󠆣󠇘󠆏󠄟󠄾󠇀︀︈󠅉󠆃󠄪󠆱︋󠇫󠄭󠄣󠆆󠄠󠅯󠆴︈󠅂󠄴︈󠆦. Did the provider mark the output in a machine-readable form?

2󠇟󠇠󠇡󠇢󠆖󠇠󠄈󠅮󠅺󠅣󠆢󠅣󠇭󠆔󠄈󠆽󠄪󠄸󠆶󠆨󠆾󠅢󠇞󠄪󠆹󠅂󠄋︈󠇪󠅾󠆾󠅐󠄪󠄚󠅯󠇤󠆬󠆝󠄜󠇣󠇣󠅶󠄔󠆦. Did the deployer give the viewer the required disclosure?󠇟󠇠󠇡󠇢󠅧︂󠆼󠇅󠇑󠆃󠄞󠆱󠄓󠄋󠅮󠇣󠇓󠇡️󠄒󠆐󠆃󠆼󠅝󠇧󠆩󠆔󠆄󠅡󠄟󠆟︍󠆄󠄃󠅐󠅇󠅱󠄖󠇛︂󠄏󠅫󠆩󠄸

A single company can face both questions, but not necessarily for the same system or use.󠇟󠇠󠇡󠇢󠇡󠆎󠅭󠄀󠆱󠆓󠄌󠅨󠇭󠆳󠅺󠄍󠄳󠄾󠅙󠇘󠅆󠅜󠄻󠄳󠆦󠅹󠆱󠆿󠆢󠄑󠇌󠇎󠅅󠆞󠄴󠄆︃󠇫󠄝󠄇󠆊󠄒󠄣󠅃

This article discusses legal developments for informational purposes only and does not constitute legal advice󠇟󠇠󠇡󠇢󠇑󠄶󠄒󠇬󠆇󠆹󠅮󠄔󠅬󠅌󠆆󠄊󠆑󠄂󠆃󠅱󠇒󠄪󠇟󠆤󠆨󠄝󠄳󠆻󠄚󠇓󠄒󠇀󠄶󠄱󠅿󠅌󠆌󠆢󠅰󠆤󠄋󠄧󠅥󠄲. Encypher is a technology company, not a law firm󠇟󠇠󠇡󠇢󠆫󠅊󠅕󠆲︅󠇋︋󠄴󠅫󠄤󠄷󠆀󠅣󠄶󠆥󠅀󠄏󠅴󠄩󠆡󠆝󠆘󠇞󠇋󠆡󠇗󠇇󠆧󠄬󠄝󠇩︄︎󠇖󠇫󠄭󠄙󠆒󠇔󠄗. Consult qualified legal counsel for advice specific to your situation󠇟󠇠󠇡󠇢󠆓󠄪󠇏︈󠆭󠅉󠆵󠆁󠆶󠇝󠅘︊󠄡️󠇯󠅸󠇕󠄒󠄹󠅴󠆥󠅳󠇮󠅒󠅝󠆆󠇝󠅍󠆾󠇫󠆯︌󠄜󠆞󠆁️󠇥󠆧󠅰󠄽.

Start with the system, not the company
"Are we a provider or a deployer?" is too broad to produce a useful answer.󠇟󠇠󠇡󠇢󠅞󠆦󠄚󠅊󠅏󠅐󠅧󠆉󠆵󠄂󠆋󠆇󠆞󠅲󠆌󠄪󠇝󠆞︂︊󠆝󠅚󠄣󠇘󠆤󠇊󠆷󠄹󠅗󠆦󠅛󠆒󠅒󠅺󠆌︆󠇐󠆰󠅜󠆩

The classification belongs at the level of a system and its use󠇟󠇠󠇡󠇢󠄪︋󠆉󠄓󠇄󠇜󠆏󠇉󠄆󠅥󠇜󠇑󠄭󠆃󠅧󠆎󠆜󠇠︋󠇝󠆺󠄋󠇉󠆆󠄅󠄉󠄷󠄱󠆵󠄑󠅎󠅅󠆛󠇙󠇫󠅪󠇏󠆑󠆛︋. A company may provide an AI writing product to customers, deploy another model in its publishing workflow, and use a third product whose vendor quietly enabled a generative feature after procurement.󠇟󠇠󠇡󠇢󠅘󠆈󠆓󠅥󠆪󠆟󠆉󠄝󠄆󠄱󠆟󠄬󠆹󠆓󠅝󠅺󠆡󠄼󠄕󠇭󠄻󠄉󠅸󠄗󠅺󠄎󠄽󠆪󠇙󠆤󠆶󠅜󠄪󠄯󠇣󠇄󠅘󠆀󠆥󠇝

That last case deserves attention󠇟󠇠󠇡󠇢󠇬󠄲︈󠄄󠇩󠆠󠆖󠄕󠄧󠆑󠅐󠅱󠅡󠄂󠆨󠇐󠄤︄󠄺󠄓󠅀󠅩󠅊󠄞󠅔󠆩󠆢󠅉︃󠅈󠇖󠆩󠇌󠅆󠆩󠅻󠄐󠇀󠆣󠇙. An inventory is only current until a vendor, model, workflow, audience, or content type changes󠇟󠇠󠇡󠇢󠆢︂󠆮󠅂󠅩󠆊󠄐󠅝󠄂󠆩󠄳󠆼󠄨󠄣󠆑󠄚󠆎󠄖󠅖󠆫󠅕󠇤󠅷󠆭󠆆󠇍󠆱󠅄󠆱󠅶󠅥󠅀󠇈󠄍󠅐󠆈󠇐󠄩󠆦󠅦. A useful register therefore needs change triggers, not just an annual review date.󠇟󠇠󠇡󠇢󠄇󠇧󠅄󠇘󠆑󠅡󠆵󠅀󠄄󠇓󠅙󠅽󠅡󠆑󠇞󠄓󠆯󠄳󠅍󠅩󠇘󠆵󠆄󠇠󠆶󠇆󠆢󠇫󠆡󠆁󠇈󠄼󠅔󠄽󠅌󠅚󠅢󠆨󠅄󠇚

I would reopen the assessment when:

- A vendor enables or materially changes a generative feature.󠇟󠇠󠇡󠇢󠅟󠆴󠇨󠅀󠇓󠆲󠆘󠆍󠄳󠄏󠅎󠄠󠄍󠆥󠆗󠇆󠅮󠇞󠅄󠄲󠅿︄󠇧󠇟︁󠄑󠅰︇󠄨󠅼󠆚󠅩󠅒󠇟󠆪󠅾󠆻󠆡󠅏󠆥

- A model or model version changes.󠇟󠇠󠇡󠇢󠄋󠆑󠆐󠆫󠇅󠄍󠅭󠆶󠅔󠆁︃󠄆󠄿󠆢󠄈󠇏󠆋󠄻󠅸󠄉󠆥󠅈︉󠇓󠇋󠆮󠅓󠅿󠇒󠆳󠄎󠄂󠆝󠅵︁󠄪󠇫󠆓︆󠆗

- The system begins producing a new media type.

- A new publication or distribution channel is added.

-󠇟󠇠󠇡󠇢󠅻󠄢󠄨󠅰󠄃󠇅󠆃󠅣󠆇󠄩󠅈󠄣󠇟󠅚󠅱󠆓󠆑󠅕󠄺󠅮󠄏󠆝󠇕󠇁󠇭󠄒󠆽󠅫󠅖󠄐󠅚󠅨󠄪󠄤󠄲󠅬󠅽󠇜󠅖󠄩 The organization uses the same system for a new purpose or audience.󠇟󠇠󠇡󠇢󠆍󠆳󠄎󠆓󠄂󠄣︉󠅌︅󠆘󠄠󠅛󠇑󠅺󠄋︎󠇥󠄋󠆃󠅅󠆡󠅊󠄽󠅕󠇩󠅲󠇜󠆥󠇚󠇃󠆼󠄉󠆌󠇅󠆓󠆝󠄎󠆊󠅛󠆂

The European Commission's AI Act Service Desk reproduces the enacted Article 50 duties:

https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50

󠇟󠇠󠇡󠇢󠇜󠅋󠅄󠄼󠆁󠆹󠅯󠇆󠄙󠄻󠆕󠆟󠇨󠆺󠇆󠇕󠄬️󠅛󠄷󠅬󠆎︄󠆺󠅩󠇔︀󠄴󠆄󠆨󠄞󠆹󠆺󠅌󠅡󠇇󠆏󠅚󠄇󠆴Run two tests, not one
For provider marking under Article 50(2), I would test the output twice.󠇟󠇠󠇡󠇢󠄻󠅢󠄜︆󠄎󠆇󠅌󠆏󠆅󠄲󠆥󠆅󠆊󠆋󠅑󠇏󠆇󠅴󠇌󠆺󠆳󠆽︁󠆱️󠇞󠆦󠆭󠄣󠇜󠅟󠆎󠆼󠅓󠄽󠆢󠆊󠄅󠅟󠆞

The first test happens at generation󠇟󠇠󠇡󠇢󠇗󠄉󠆮󠆴󠅞󠄓󠄟󠆛󠅜󠇈󠆰󠇍󠆈󠅫󠄇󠆝󠆶󠄯󠄺󠅅󠄯󠅠󠅳󠆁󠆊󠅏󠅍󠆇󠄖󠇝󠆢󠆞󠄛󠇪󠅨󠆖󠅋󠇢󠆺󠆢. Does the production system emit an output that carries a machine-readable mark and can an independent verifier detect it?󠇟󠇠󠇡󠇢󠇩󠇧︃󠄖󠇟󠆑󠇍󠄋󠆆󠄫󠆮󠇛︂󠅤󠅡󠅺󠅁󠄡󠅦󠅟󠆶󠆑󠆙󠅌󠄨󠄔󠅕󠅙󠆇󠄲󠄡󠇢󠆻󠅿󠇩󠅰󠇬󠆅󠇘󠅷

The second test happens at the published endpoint󠇟󠇠󠇡󠇢󠄿󠄍󠄠󠆂󠇌󠆽󠄔󠇚󠆐󠅟󠆀󠄉󠅨󠅗󠅃󠄞󠇑󠅸󠅈󠆕󠄆󠆻󠄷󠅹󠅗󠆭󠆹︍󠇘󠇖󠇒︋󠄒󠄗︊󠆼󠇤󠆨󠄈󠇒. Does the same mark remain detectable after the CMS, API, export, re-encode, resize, transcode, upload, or platform processing that users actually encounter?󠇟󠇠󠇡󠇢󠅟󠇊󠄼󠇮󠆌󠅱󠆆︄󠆝󠄧󠄎󠅿󠄂󠄝󠄷󠅭󠆲󠇆󠇩󠅪︊󠅍󠄉󠅴󠇯󠄎󠇙󠄷󠄨󠅰󠇝󠇋󠅀󠇡󠆧󠄱󠇚󠄹󠆔󠄺

A successful generation-time test does not answer the endpoint question󠇟󠇠󠇡󠇢󠄫󠆶󠄊󠇜󠄱󠇙󠄀󠅌󠇍󠅢󠇄󠇖󠆰󠆏󠅢󠅽󠄴󠅎󠇙󠆸󠅈󠄹󠄷󠆸󠅶󠇝󠅭󠄡󠇈󠇬󠄙󠄖󠆽󠅠︃󠄡󠆨󠄩󠄘󠅍. Many implementation failures are silent: the pipeline produces a valid asset, but the transformation removes the provenance data without raising an error.󠇟󠇠󠇡󠇢󠆼󠅋󠅞󠄀󠅹󠄉󠅁︅󠄂︅󠆆󠆇󠇗󠅛󠇪󠄗󠄑󠄙󠄿󠆍󠆤󠅭󠆗󠅓󠅤󠇨󠅮󠇞󠄈󠄲󠄽󠆵󠅮󠄕󠆛󠇍󠄠︊󠅪󠄎

The deployer test is different󠇟󠇠󠇡󠇢︊󠇫󠆇󠄦󠆻󠄳󠅆󠄊󠆳󠆙󠄁󠅜󠇪󠅀󠅻󠅃󠅪󠄡󠅅󠅱󠆝󠅛󠅖󠄶󠇒󠅠󠆇󠅫󠆑󠅆󠇊󠆣󠆱󠆨󠇂󠆧󠄎󠄷󠇖󠆻. For deepfakes and covered public-interest text under Article 50(4), I would load the real page, app, player, or feed and record what the viewer sees at first exposure󠇟󠇠󠇡󠇢󠅒󠇫󠄔︈󠆪󠄷󠆮󠄂󠄀󠆿︁󠅅󠄻󠇭󠇂󠄳󠆢󠆡󠄭󠄰󠆦󠄂󠆟󠄜󠅑󠆌︅󠅻︄󠅾󠆾󠇮󠇃󠆬󠆒󠇒󠆰󠅜󠄾󠄅. A hidden machine-readable mark cannot replace a required human-facing disclosure.󠇟󠇠󠇡󠇢︆󠆄︂󠆩󠄑󠆇󠄩󠄔󠅆󠇊󠆩󠄮󠄩󠄉󠄟󠄅︁󠇬󠅕󠄮󠄻󠅟󠆿󠄍󠆃󠇫󠅧︄󠇩󠆁󠆱󠄰󠄙󠅥󠆹︍󠄱󠄶󠅾󠄐

The cleanest evidence package therefore contains both technical verification and a dated capture of the user experience.󠇟󠇠󠇡󠇢󠅪󠇏󠅟󠅳󠇘󠅩󠆶󠄊󠅾︊󠄥󠅨󠆥︂󠆖󠇥󠇒︌️󠄚󠇚󠆦󠆞󠇡︎󠄀󠆛󠇌󠆲󠄛󠄍󠅰󠆳︌󠄩󠇟󠅼󠇡󠄺󠇂

Treat exceptions as claims that can expire
An exception should not sit in a register until the next annual review simply because someone approved it once.󠇟󠇠󠇡󠇢︃︆󠄝󠆂󠇓󠄮󠄥󠄳󠄻󠇓󠄬󠄡󠇬󠅈󠇜󠆩󠆅󠄢󠄖󠆽󠄤󠆪󠇝󠆕󠇫󠇙󠆒󠄢󠄪󠅑󠄧󠅼󠅡󠆊︌󠅧󠆩󠄳󠅞󠆙

The facts supporting an exception belong to a particular system, configuration, workflow, and use at a particular time󠇟󠇠󠇡󠇢󠅝︇󠆕󠆞󠄃󠅏󠆅󠇁󠄮󠇧󠆊󠆃󠆐󠇧󠅧󠅫︇︁󠆄󠄼󠆆󠅳󠄎󠅡󠇉󠄛󠄶󠄽󠆙󠆊󠅊󠄟󠄥󠅍󠆠󠄨󠆳︊󠆔󠅔. If one of those facts changes, the organization should reopen the assessment.󠇟󠇠󠇡󠇢󠅡󠆚󠆖󠇟︈󠆹󠅐󠄡󠅼󠄍󠅰󠅳󠇉󠅫󠇜︋󠄽󠆆󠅔󠆤󠅉󠄢󠄉󠆔󠄲󠆨󠆏︌󠄮󠄖󠄟󠄼󠇟󠄧󠄾︅󠅯󠆇󠅋󠄪

For AI-generated public-interest text, the record should identify the human review or editorial control performed and the natural or legal person holding editorial responsibility󠇟󠇠󠇡󠇢󠇐󠇬󠇂󠅛󠇎󠇯󠅥󠄽󠆥️󠆘󠅙󠆷󠆻󠇘󠄟󠇡󠇪󠆊󠄖󠄡󠅰󠆰󠇎󠆬󠄪󠅍󠆊󠄄︆󠆨󠆮󠅗󠄿󠆦󠆅󠄖󠇠󠄌󠅰. It should also name the events that force reassessment.󠇟󠇠󠇡󠇢󠆑󠅲󠅣󠆡󠄘󠄮󠆰󠆚󠆝󠄪󠆿󠆞󠄡󠄭󠄀︁󠇆󠅟󠅪󠆽󠅉󠄊󠇧󠇇󠆊︀󠄃󠆆󠆗󠆓󠅃󠅄󠆳󠆈󠆱󠇌󠆕󠄸󠅑󠆽

The same principle applies to artistic, creative, satirical, fictional, and law-enforcement circumstances󠇟󠇠󠇡󠇢󠄆󠅂󠅜󠄒󠆺󠆰︊󠅿󠅷󠄨󠄈󠆯󠄺󠄤󠆯󠄥󠄢󠄃󠇈󠆙󠄈︁󠇜󠇍󠅭󠅘️󠆑󠅰󠄾󠄶󠇏󠇂󠅣󠄕󠄃󠆃󠆼󠅕󠅀. Record the facts and the owner, then define when the conclusion stops being safe to reuse.󠇟󠇠󠇡󠇢󠄢󠄑󠄨󠇭󠅽󠄶󠆘󠄫󠆱󠄖󠇑󠇘󠆁󠅻󠄴󠄢󠆋󠅨󠄫󠅠󠇇󠅲︆󠇡󠅳󠅢󠄰󠅭󠅽󠄠󠆚󠆅󠇆󠄡󠄦󠆷󠄡󠇁󠆙󠄇

󠇟󠇠󠇡󠇢󠇟󠇮󠇀󠅾󠅒󠆳󠇉󠇌󠅃󠅥󠆑󠆱󠇥󠅩󠄿󠆣󠅲󠄘󠄴󠅱︂󠅑󠆦󠄧󠄍󠄭󠅘󠅑󠆠󠅎󠅠󠄢󠄙󠆩󠅋󠇬󠇢󠇊󠆏󠅅What I would put in the day-one file
I would keep the file short enough that an operating team can maintain it󠇟󠇠󠇡󠇢󠅇󠅎󠇐󠇯󠄸󠆿󠆆󠄡󠇬󠅻󠄛󠅎󠅫󠇪󠇜󠆠󠅁󠇥󠄬󠆊󠇌󠆔󠇤󠆯󠇭󠇀󠇜󠇧󠅷󠆪󠅴︀󠅠󠄆󠆖󠄌󠅨󠄋󠇜︄. For each system and use, it should contain:󠇟󠇠󠇡󠇢󠄕󠅊󠆀󠇌󠄀󠄘󠆤󠆦󠄺󠅄󠄳󠅷󠆋󠅆󠄄󠅘󠆥󠅿󠇎󠅄󠅤󠅼󠄋󠅚󠅲󠅫󠆶󠆈󠅚󠅚󠆉󠇤󠅟󠇪󠆅󠅓︎󠅢︋󠅵

1. System identity󠇟󠇠󠇡󠇢󠇤󠅢󠇈󠄋󠅘󠄢󠅡󠆞󠅠︀󠇯󠄍󠄞󠅵󠆂󠄥󠆚󠄊󠆛󠆤󠆄󠅛󠄙󠆲󠅑󠄥󠇈󠅧󠄞󠅗󠅾󠇅󠅛󠅩󠅊󠇀󠅿󠅹󠅽󠄏.󠇟󠇠󠇡󠇢󠄀󠅼󠇜󠆸󠆤󠄊󠆇󠇏󠄭󠅦󠅟󠄹󠄰󠅹󠆼󠇇󠇄󠆖󠄭︀󠆅󠆦󠄦󠆯󠄛󠄦󠇞︅︌󠄹󠅨󠅳󠆳󠅵󠅔󠅬󠄎󠅎󠆪󠇘 Product, model, version, owner, content types, users, markets, and current configuration.󠇟󠇠󠇡󠇢󠅹󠆈󠅏󠇛󠄳󠅑󠆄󠆿󠇄󠇊︅󠅄󠆬󠇊󠇅󠄴󠄙󠅑󠇭󠅛󠇮︅󠅠󠆼󠄁󠆩󠅥󠆤󠆴󠇔󠅝󠅊󠅏󠆯󠆧󠆖󠄵󠄳󠅶󠇒

2. Role and duty󠇟󠇠󠇡󠇢󠅺󠇫󠅴󠄂󠆠󠄑󠆫󠅙󠇢󠅝󠄘󠅃󠄘󠆽󠅖󠇯󠆈󠄅󠅍󠅕󠅌󠆨󠆶︎󠇕󠄚󠄵󠆯󠄰󠅟󠄇󠇭󠆜󠆪󠇃󠄴󠅚󠆅󠅴󠆟.󠇟󠇠󠇡󠇢󠄦󠄳󠄋󠇫󠆖󠇓󠄾󠅕󠆚󠄽󠄭󠅴󠇈󠅍󠆪󠇙󠆘󠆁︂󠅽󠇏󠅮︈󠆰󠇓󠇓󠅈󠇧󠆼︁󠄧󠆗󠇆󠆜󠆢󠇣󠄽󠅚󠅼󠆾 Provider, deployer, or both, with the relevant Article 50 paragraph and system-specific analysis.󠇟󠇠󠇡󠇢󠄬󠄰󠆆︃󠅆󠇌󠇅󠄣󠇄󠆞󠄯󠅀󠆀󠆬󠅒󠇔󠆎󠄎󠇋󠄐󠆡󠄐󠅼󠄞󠄷󠆭󠇝󠄸󠆮󠆭󠄠󠅯󠆼󠄺󠆶󠄐󠆐󠄊󠆛󠄀

3. Generation test󠇟󠇠󠇡󠇢󠇬󠄕󠇁󠆢󠆀󠆯󠆾󠆍󠅴󠄋󠇂󠇎󠄂󠅔󠇘󠅈󠆵󠇎󠄄︎󠄈󠇊󠅄󠆃󠅈󠅉󠄾󠄧󠅦󠆶󠅋󠄀󠅣︎󠆼󠅵︂󠆃󠅤󠆵.󠇟󠇠󠇡󠇢󠄗󠅝󠆍󠅦󠇘󠆂󠅰󠅡󠅷󠆟󠆮󠇫󠆫󠆍󠇢󠆌󠆗󠅨󠇄︅󠇫󠄾󠇟󠄸󠄑󠄤󠅀󠄰󠄞󠄸󠄍︋󠇣󠅴󠄋󠅿󠅓󠄜󠆏󠅅 A dated production sample and the result of machine-readable verification.󠇟󠇠󠇡󠇢󠄬󠆞󠆂󠅚󠇍󠆌󠇙󠄑󠅓󠅩󠄟󠆞󠄘󠇬󠅮󠅕󠆥󠇂󠄎󠇪󠄎󠄌󠆘󠆊󠄀󠆋󠇤󠄥󠄒󠄸󠇠󠅥󠄸󠇧󠄋󠅰󠅼󠄬󠅰󠆥

4. Endpoint test󠇟󠇠󠇡󠇢󠇦󠅪󠄟󠇄󠆴󠇠󠅋󠅦󠅬󠇎󠆻󠇩󠅃󠇑󠆎󠅤︃󠆀︆󠄙󠇢󠄎󠇦󠅞󠆊󠄧󠆌︎︉󠆨󠄅󠆐󠅢󠆷󠅵󠅹󠇠󠄢󠄏󠄡.󠇟󠇠󠇡󠇢󠆰󠆯󠇉󠅣󠅞󠇧󠆻󠇭󠆧󠅏󠆾󠆮󠆴󠅷󠄃󠇅󠅄󠆭󠄟󠆎󠆞︃󠆂󠅯󠄢󠇮󠄪󠄢󠅋󠄼󠆑󠄴󠇡󠇎︄󠅌󠅆󠆴󠆃󠄯 The same sample after the real publication and distribution route, verified again.󠇟󠇠󠇡󠇢️󠄳󠄘︅󠆇󠇍󠄾󠄱󠅔󠅥󠇃󠇝󠄳󠇩󠅆󠄳󠆄󠄋󠇄󠇐󠅥󠇣󠅃󠅥󠅷󠆓︄󠆭󠅱󠅄󠆡󠆔󠆤󠅢󠄘󠅱󠄨󠅅󠇤󠄄

5󠇟󠇠󠇡󠇢󠆱󠆕󠆿󠅢󠇮󠇜󠆹󠅲󠅉󠆥󠅤󠄰󠆌󠄴󠆣󠅸󠅽󠆨󠄷︂󠄶󠄀󠅱󠅵󠄬󠅯󠆳󠇞󠇤󠆮󠇆︉󠆷︅󠅡󠄰󠄗󠇯󠅹󠆰. Viewer test󠇟󠇠󠇡󠇢󠄲󠅨󠆰󠄉󠄉󠇠󠅳󠄧󠅚󠆈󠅘󠅍󠇔󠅱󠅶󠄍︇󠇎󠄅󠅨󠇨󠅵󠅄󠄨󠇛󠆛󠄐󠇊󠅵󠅔󠄈󠆥󠄒󠇦󠅱󠄎󠇕󠇦󠅞󠇒.󠇟󠇠󠇡󠇢󠆒󠇕󠅑󠇞󠄍󠅨󠄑󠆬󠅶󠇦󠄫󠅈󠇨󠇞󠇒󠆁󠆏󠇦󠄯︊󠄤󠄽󠅩󠇓󠇡󠄠󠅐️󠄖󠅊󠅧󠄤󠆄󠇚︄󠄪︁󠆟󠄙󠆟 A screenshot or recording of the disclosure shown at first exposure where a deployer duty applies.󠇟󠇠󠇡󠇢󠄨󠆆󠆩󠄎󠅇󠅫󠄫󠆡󠄫󠅃󠅨󠅵󠅠󠆄︋󠆎󠅫󠇭󠅿󠆀󠇑󠆠󠅉󠇠󠆸󠇁󠅽󠆭󠇅󠆟󠅙󠇌󠇕󠄆󠆾󠄚󠅌󠄤󠆳󠅠

5. Exception record󠇟󠇠󠇡󠇢󠇫︊󠆬󠅰󠄵󠅽󠆰󠅁󠄴󠆰󠅹󠆄󠅑󠅎󠅪󠆂󠅘󠅘󠆒󠆇󠆟󠇀︂󠄞󠄲󠄔󠆢󠇧󠇃󠆩︈󠇗󠇐󠆔󠆻󠄕󠆀󠅪󠄁󠄻. Supporting facts, review performed, editorial responsibility, owner, approval date, and reopening triggers.󠇟󠇠󠇡󠇢󠇖󠅏󠆀󠆺︇󠇦󠆃󠅭󠄁󠄺󠆲󠇌󠆛󠄨󠆼󠄠󠄔󠆴󠅄󠆲󠆍󠄄󠅼󠅫󠅬︄󠆉󠆘󠆚︄󠄏︅󠅅󠄪󠄅󠇔󠅾󠅉︀󠅚

6. Failure history󠇟󠇠󠇡󠇢󠇚󠅴󠅆󠇅︈󠅪󠅁󠇔󠅜󠄴󠄲󠅦󠇚󠄶󠆰󠆲󠆀󠄸󠆌󠆱󠅘󠅵󠇉󠄁󠇪󠅑󠇆󠇛󠅡󠄟󠇧󠆙󠄂󠆒︎󠇏󠅦󠇫󠄖󠅄. Failed samples, affected routes, fixes, control versions, and retest dates.󠇟󠇠󠇡󠇢󠇋󠄶󠆦󠅜󠅏󠆂󠄫󠇅󠆅󠇚󠇮󠆨󠇪󠅖󠄱󠇤󠄳󠄧󠅶󠅛󠆷󠆌󠇠󠅁󠄛󠆰️󠅚󠆽󠅿󠆊󠄪︍󠄘󠄤󠅉︇󠄬󠄚󠄒

The file should answer a practical question without a meeting: what ran, which duty applied, what was tested, what failed, and who owns the next action?󠇟󠇠󠇡󠇢󠆡󠄚󠄮󠅥󠄺󠆴󠆾︊󠆲󠇒󠄫󠄳󠄼󠆔󠄆󠅢󠅧󠆯󠅴󠆮󠇀󠆯︊󠆃󠆣󠄡󠄌󠅒󠇤󠆌󠇅󠇔󠅥󠄌󠆾󠅌󠆭󠆥󠆼󠇀

Encypher's readiness check provides a structured starting point:

https://encypher.com/tools/eu-ai-act-readiness

Use the Code of Practice as an engineering map
The Code of Practice is voluntary󠇟󠇠󠇡󠇢󠅧󠄮󠄢️󠅽󠄑󠆫󠅶󠅱󠅓󠄷󠅵󠅬󠆙︄󠆅︂󠅀󠆲󠆗󠅍󠇦󠄽󠇃󠇠󠆦󠄽󠄓󠆨󠄴󠄅󠆤󠅸󠆅󠇡󠆹󠄟󠆵󠇉󠇐. The Article 50 obligations are not.󠇟󠇠󠇡󠇢󠇈󠆲󠄻󠇅󠆫󠄟󠇥󠄙󠄸󠅬󠆡󠆐󠆺󠆇󠇅󠄊󠇎󠆕󠆞󠄰︌󠅶󠄼󠅄󠆃󠅅󠅑󠇞󠆇󠆇󠇌󠄓󠄰󠇡󠄲󠅵󠆯󠄱󠆄󠇆

That distinction matters because the Code is useful even for an organization that does not sign it󠇟󠇠󠇡󠇢󠆾󠄧󠄊󠅆󠄔󠆺󠅸󠆦󠆏󠄡󠅡󠇞󠆎󠇃󠇜︇󠄥󠇮󠅌󠄔󠅫󠆝󠄥︊󠆕󠅑󠄧󠆘󠄏󠅉󠇖󠇅︃󠄍󠄛󠇤󠆈󠄸󠆝󠄪. It separates provider marking and detection from deployer labelling, then translates those duties into measures that technical and governance teams can test.󠇟󠇠󠇡󠇢󠄮󠇕󠇙󠄿󠆀󠇅󠆤󠅜󠅖󠄴󠄆󠄪︁󠆨󠆏󠆖󠄱󠄥󠆐󠆢󠆘󠅣︄󠄭󠆟󠄀󠇤󠅘󠅇︃󠇏󠅵󠄳󠅍󠇌󠅁󠇓󠇒︌󠅉

For marking, the final Code recommends a layered approach: digitally signed metadata, such as C2PA provenance, together with imperceptible watermarking󠇟󠇠󠇡󠇢󠆗󠇭󠄬󠆮󠇣󠇤󠄐󠆇󠄬󠅘󠄎󠄟󠇅󠇬󠄆︁󠆂󠆜󠄛󠅛︇󠅗󠄖󠇬󠆅󠆲󠇊︋󠅎󠆕󠆡󠄲󠇜󠅈󠇥󠆓󠇑󠄐󠆛󠇡. Fingerprinting or logging can add another layer.󠇟󠇠󠇡󠇢󠆽󠅹󠅞︁󠅓󠆂󠄉󠄜︋󠅁󠇟󠅟󠆣󠆓󠅧︍󠅺󠆪󠇔󠄨󠇥󠆱󠄇󠆜󠆜︊󠆧󠄪󠄧󠆘󠄤󠄩󠅘󠄝󠇂󠅣󠆥󠆂󠅲󠆴

The point is not to collect technologies󠇟󠇠󠇡󠇢󠆶󠄱󠄒︂󠄿󠄎󠄯󠄈󠆻󠄶󠆜󠆈︎󠆂󠇚󠆵󠇂󠅚󠆉󠆁󠅌︇󠇣󠇒󠅭󠅌󠆎󠇢󠄢︉󠇫󠄽󠇅󠆣󠆹󠆘󠅥󠅙󠄎󠇔. Each layer covers a different failure mode󠇟󠇠󠇡󠇢󠄳󠇬󠄼󠄧󠆖󠅽󠇏󠆴󠅚󠅸󠄨󠇥󠇪󠇣󠅅󠆴󠄘󠇅󠅤󠅍󠄠️󠆺󠇈󠅡󠄡󠆾󠅗󠇔︃󠅛󠇑︋󠇍󠅡󠆖󠆍︀󠇈󠅪. Signed metadata can carry detailed, verifiable provenance but may be removed by a downstream transformation󠇟󠇠󠇡󠇢󠄣󠄤󠅔󠇚󠇯󠄆󠄕󠇬󠄥󠅞󠇢󠆇󠄍󠆆󠅭󠇥󠆳󠇅󠅏󠆵󠇚󠅢󠇞󠇁󠄶󠄗󠅰󠆯󠄥󠅜󠅙󠆜󠇋󠄼󠆹󠄰󠆻󠄲󠄌󠇖. A watermark may survive some transformations while carrying less information󠇟󠇠󠇡󠇢󠅠󠇕󠄩󠅴󠄡󠆣󠇞󠅌󠆫󠄛︁󠇏󠅗󠄛󠄌󠄧󠆕󠆫︅󠄳󠄃󠆼󠆼󠆤󠄟󠆕󠆳󠅀󠆒󠄫󠅽󠇊󠅻󠄤󠄾󠄀󠅟󠇪󠄂󠅯. The implementation still has to work across the organization's actual content routes.󠇟󠇠󠇡󠇢󠄬󠅑󠆝󠄚󠆝󠇜󠅚︆󠅾︍󠆎󠄺󠇭󠇫󠄥︃󠅲󠄾󠅱󠅃󠄊󠅆󠅫󠅮️󠆀󠆑󠄡󠅧󠇓󠄼󠄙󠆨󠆭󠄳󠆄󠇜󠄑󠇞󠆸

The Commission's page for the final Code is here:

https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content

Where C2PA fits
Article 50 does not prescribe C2PA󠇟󠇠󠇡󠇢󠆫󠄲󠄍󠄑󠇡󠅑󠆯󠆗󠅼󠄊󠅦󠇏󠄴󠇍󠆾󠆪󠆡󠆆󠄠󠆔︌󠄔󠅜󠇃󠇍󠄨󠇬󠇮󠇁󠅝󠅉︍󠅃󠄝󠅵󠇣󠆋︅󠆖󠅴. It states a technology-neutral machine-readable marking requirement.󠇟󠇠󠇡󠇢󠇠󠇉󠆝󠅫󠅧󠅚󠆀︊󠇕󠆅󠆶󠅫󠇝󠆂󠅥󠇊󠄋󠄬󠆀󠆴󠇖󠆳󠄘󠆘󠄩󠄷󠆏󠅮󠄡󠅞󠄮󠇊󠄍󠅹󠇨󠆺󠆉󠆼󠄀󠅤

C2PA provides an open way to attach signed provenance claims to content󠇟󠇠󠇡󠇢󠆼󠇃󠅎󠅫󠅭󠄢󠄻󠄖󠇛󠄼󠆏󠄖󠄙󠅓󠄗󠇔󠅸󠄓󠇔󠄴󠇀󠄽󠇐󠆗󠆽󠄟󠅄󠅒󠄈󠇐󠄑︇󠇙󠄕󠅀󠅂󠇪󠇜󠄆󠆊. Used correctly, it can identify an output as AI-generated, carry source and integrity information, and give downstream systems a signal they can use when displaying a disclosure.󠇟󠇠󠇡󠇢️󠄨󠆉󠇬󠆦󠄅󠆁󠇀󠅰󠆣󠅖󠆉󠄩󠅥󠆱󠇞󠄽󠇜󠆉󠄜󠅌󠆌󠆫󠆚︌󠆮󠆈󠇘︊󠆤󠅬󠅾󠅅󠇁󠆒󠅩󠄿󠄇󠆭󠇞

It does not establish that a claim is true merely because it is signed󠇟󠇠󠇡󠇢󠆹󠆆󠄺󠇒󠅿󠅉︋󠇋󠄑󠇟󠅅󠅄󠆀󠄚󠇡󠆓󠆵︂󠄸󠇩󠇫󠇪󠄻󠇠󠆶󠅚󠆬󠄷󠆂󠅒󠆼󠅝󠅌󠄤󠆱󠄕󠆟󠄜󠆊󠅹. It does not prevent every platform from removing the mark󠇟󠇠󠇡󠇢󠄁󠆋󠄞󠇚󠇇󠆭󠄶󠄝󠄛󠆉󠄜󠇓󠇃󠅥󠇗󠄌󠆼󠅍󠄞󠄝󠅟󠅭󠅰󠆋︇󠄹󠆦󠅠󠄚󠇒󠄘󠅂󠆾︄︄︁󠄴󠄰󠇁󠇄. It does not turn a technical integration into a legal conclusion.󠇟󠇠󠇡󠇢󠆺󠆦󠆕󠅙󠆎󠄪󠄠︋󠇊󠆌󠅪󠄭󠅋󠇞󠄃︂󠅯󠆝󠆤󠄴︄󠄽󠄘󠇬󠆊󠄀󠆌︂󠅒󠄣󠇡󠇦󠅕󠄷󠄫󠆓󠇈󠅓󠄦󠄰

That is why I would treat C2PA as part of a tested control rather than as a compliance label.󠇟󠇠󠇡󠇢󠄿󠅃󠅈󠇯󠆴󠅁󠇞󠇮󠆞󠆼󠆀󠄧󠆏󠇖󠅿󠅌󠅲󠅕󠇖󠇇󠅅󠄖󠇛󠇑󠅅󠅓󠄲󠇐󠇐󠆼󠄱󠅓󠄶󠆛󠄏󠄺󠆊󠄗󠆖󠆷

A standard C2PA manifest applies to the document as a whole󠇟󠇠󠇡󠇢󠇩󠇂󠄡󠆶󠆅︌︄󠅁󠄲󠇧󠇢󠅘󠆛󠅁󠅗󠅮󠄚󠄂󠅲󠄬󠆤󠅜󠆵󠅇󠆲󠅃󠆍󠅻󠇩󠅟󠄊󠅒︇󠅞󠇦󠅝󠄝󠆁󠅵󠆢. Encypher's proprietary text technology adds sentence-level attribution󠇟󠇠󠇡󠇢󠅼󠇕󠅉󠆔󠄺󠆘󠄪󠆓󠆇󠄊󠆊󠅰󠄞󠇢󠇔󠄎︅󠇊󠆰󠅦󠆿󠆿󠆱󠄎󠅈󠅠󠅗󠅀󠇏󠄆󠅂󠅲󠄻󠆀󠅪󠅎󠄠󠄎󠄐󠄏. Encypher also authored the C2PA unstructured-text provenance appendix, Section A.7 in C2PA 2.3 and Section A.8 in C2PA 2.4.

Five questions for Monday morning
I would ask the operating team:

1󠇟󠇠󠇡󠇢󠄔󠄍󠇔󠆌󠄹󠆛󠆔󠇄󠄙󠇎󠅌󠆟󠆯󠄤󠅜︍󠇤󠄴󠄌󠅒󠄠󠅗󠄐󠅧󠅂󠅆︋󠇑󠆐󠇌󠇉󠄴󠇂󠆥󠅐󠄇󠆮󠄹󠄚󠄡. Which production systems changed since the inventory was last approved?

2󠇟󠇠󠇡󠇢󠇖󠄔󠇔󠅽󠆪󠄫󠆚󠅐︁︀󠆁󠅈󠅐󠆫󠆑󠄢󠅺󠄴󠆔󠄥󠇢󠅂󠇆󠄠󠄔󠆴󠄽󠆒︍󠆘︀󠆈󠄄󠄚󠇂󠄠󠄚󠄻󠅞󠆈. Can we verify a marked output both at generation and at the public endpoint?

3󠇟󠇠󠇡󠇢󠄜󠇁󠅕󠇜󠅴󠆟󠄔󠄀󠅆󠆛󠇨󠆿󠆄󠄒󠅸󠆉󠅉󠆓󠅉󠇨󠄬󠄟󠅙󠄗󠅬󠆺︍󠄑󠇒󠄍󠄘︂󠆎󠄅󠇫󠅹󠅜️󠅓󠆦. Can we show what the viewer sees when a deployer disclosure applies?

4󠇟󠇠󠇡󠇢󠆕󠅊󠄏󠅬󠆒󠅶󠇌󠆺󠇥󠄒󠆀󠆘󠄇󠇆󠄋󠇪󠇧󠆂󠄠󠅽󠆚󠅏󠆈󠅺󠅂󠆹󠆧󠄻󠄉󠄹︉󠆉󠅝󠅦󠇒󠅾󠇪󠇠️󠅻. Which exceptions reopen after a model, vendor, workflow, or use change?󠇟󠇠󠇡󠇢󠄳󠆈󠅬󠄫󠅬󠇩󠇪󠄲󠆍󠄟󠇃󠆉󠇮󠇨󠆮󠄫󠇛󠇫󠄷󠅽︃󠅛󠄆󠅷󠄎󠇯︎󠆤󠆹󠅯󠅌󠆹󠄭󠄾󠅤󠅲󠇛󠆣󠅛󠄧

5󠇟󠇠󠇡󠇢󠅓󠇓︉󠄚󠄙󠄦󠄡󠆤󠄯︌󠆱󠄋︇󠄼󠄽󠄕󠆭󠄋󠇙︂󠄘󠆵󠄌󠇙󠇋󠅳󠆱󠄒󠄻󠄿󠆨󠅰󠇤󠄛󠅮󠆥󠅋󠆔󠆸︂. Who can stop or repair a route when the mark or disclosure fails?󠇟󠇠󠇡󠇢󠇄󠄀󠅞󠇨󠇦󠅛󠅡󠄋󠄯󠆏󠆂󠄨󠇂󠆜︄󠅹󠄫󠆁󠇇󠅿󠅡󠇬︉󠅶󠆹󠆙󠅑󠅋󠄮︈󠆚󠇨󠆐󠄷󠆴󠆍󠆯󠄏󠄶󠆺

A policy can describe the intended control󠇟󠇠󠇡󠇢󠆺︇󠄝󠆀󠅭󠄛󠇏󠅷󠇏󠄅󠄏󠄼󠆏󠅑󠅊󠇚󠆗󠇅󠅜󠅈︀󠆐󠅅󠆿󠇋󠅂󠅻󠄺󠅌󠆜︆󠇀︆󠆙󠄦󠄘󠇮︂󠇧︁. The day-one file should show that the control survived contact with the production system.󠇟󠇠󠇡󠇢󠆿󠅧󠇃󠄷󠆢󠅛󠄕︊󠇬󠅱󠅃︎󠆽󠅭󠇢󠄖󠅢󠅵󠄱󠇝󠅍󠅟️󠅫󠅆󠅼󠆮󠄘󠄴󠆓󠆆󠇒󠆋󠇉󠆚󠄘󠄠︄󠄶󠇞

"""

result = final_chain.invoke({"text": text})
print(result)

final_chain.get_graph().print_ascii()
