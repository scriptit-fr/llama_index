# Writing Custom Modules

A core design principle of LlamaIndex is that **almost every core module can be subclassed and customized**.

This allows you to use LlamaIndex for any advanced LLM use case, beyond the capabilities offered by our prepackaged modules. You're free to write as much custom code for any given module, but still take advantage of our lower-level abstractions and also plug this module along with other components.

We offer convenient/guided ways to subclass our modules, letting you write your custom logic without having to worry about having to define all boilerplate (for instance, [callbacks](/module_guides/observability/callbacks/root.md)).

This guide centralizes all the resources around writing custom modules in LlamaIndex. Check them out below 👇

## Custom LLMs

- [Custom LLMs](using-custom-llm-advanced)

## Custom Embeddings

- [Custom Embedding Model](custom_embeddings)

## Custom Output Parsers

- [Custom Output Parsers](/examples/output_parsing/llm_program.ipynb)

## Custom Transformations

- [Custom Transformations](custom-transformations)

## Custom Retrievers

- [Custom Retrievers](/examples/query_engine/CustomRetrievers.ipynb)
- [Custom Knowledge Graph + Vector Retriever](/examples/index_structs/knowledge_graph/KnowledgeGraphIndex_vs_VectorStoreIndex_vs_CustomIndex_combined.ipynb)

## Custom Postprocessors/Rerankers

- [Custom Node Postprocessor](custom-node-postprocessor)

## Custom Query Engines

- [Custom Query Engine](/examples/query_engine/custom_query_engine.ipynb)

## Custom Agents

- [Custom Agents](/examples/agent/custom_agent.ipynb)

## Custom Query Components (for use in Query Pipeline)

- [Custom Query Component](query-pipeline-custom-component)

## Other Ways of Customization

Some modules can be customized heavily within your workflows but not through subclassing (and instead through parameters or functions we expose). We list these in guides below:

- [Customizing Documents](/module_guides/loading/documents_and_nodes/usage_documents.ipynb)
- [Customizing Nodes](/module_guides/loading/documents_and_nodes/usage_nodes.ipynb)
- [Customizing Prompts within Higher-Level Modules](/examples/prompts/prompt_mixin.ipynb)
