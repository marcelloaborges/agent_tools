<b>Langchain Tool Calling agent</b>

This test idea is to build an agent capable of calling tools that are handled by auxiliary LLMs.

A main model with a higher interpretation capacity will handle the user request and keep the chat flowing meanwhile the tools have a smaller LLM supporting the processed requests tasks.<br>
For simplicity and to speed up the results, a local service is being used to expose the auxiliary LLM through the LM Studio. The model downloaded is the <b>Meta-Llama-3-8B-Instruct-Q4_K_M</b>.<br>
The request flow happens the following way:
 - The user makes a request.
 - The agent handles the request and identifies which is the best tool to solve the task.
 - The selected tool has a smaller LLM model responsible for processing the task which can be evolved to a bigger one in a further update, combined with database queries, etc.
 - The tool result is used by the agent to formulate the final answer and present the results to the user.

The jupyter notebook has a simpler version handling the functionality.

To execute the code, run the <b>main.py</b> which exposes a simple REST API that can be used through Postman or any other tool.
The API has only two routes:
  "/": returns the default message to explain what the agent does.
  "/chat": handles the the user requests.

Considerations:
 - The current version doesn't have chat history or memory management. This is going to be implemented in a future update.
 - In case of not using LM Studio for the auxiliary LLM, change the LLM model at the <b>tools.py</b> file to the one of your choice.

API request examples:
 - "/":
   - <b>GET</b> with no params.
 - "/chat":
   - <b>POST</b> with JSON body:
     - {
        "user_input": "Lyra, any buffs for Pantheon last patch?"
      } 
