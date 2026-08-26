# AI Core Concepts

## What is Artificial Intelligence (AI)
AI is the field of making computers do tasks that seem smart when humans do them. Old AI followed hand-written rules. Modern AI learns patterns from examples instead.

## What is Machine Learning (ML)
Machine Learning is a part of AI where the computer learns from data instead of being given explicit rules. You show it thousands of examples and it figures out the pattern by itself.

## What is a Large Language Model (LLM)
An LLM is an AI trained on huge amounts of text to predict the next word. ChatGPT works by reading your question and generating the most likely next words, one token at a time.

## What are tokens
Tokens are the pieces of text a model reads. A token can be a whole word or part of a word. LLMs do not read words, they read tokens.

## What are embeddings
Embeddings are lists of numbers (vectors) that represent the meaning of text. Text with similar meaning gets vectors that sit close together in space. This lets a computer search by meaning, not just keywords.

## What is RAG
RAG stands for Retrieval-Augmented Generation. It first retrieves the most relevant chunks from your documents, then gives those chunks to the LLM so it answers based on your data instead of only its memory.

## Difference between embeddings and RAG
Embeddings are the building block: numbers that represent meaning. RAG is the full pipeline that uses embeddings to search documents and then feeds the results to an LLM. Embeddings = the tool. RAG = the system built with it.

## What is chunking
Chunking is splitting long documents into smaller pieces before embedding them. Smaller chunks make search more precise, because the AI retrieves exactly the relevant part instead of a whole page.

## What is an AI agent
An agent is an AI that can use tools and take actions, not just generate text. It can call a calculator, search the web, or query a database, then continue reasoning with the results.

## What is hallucination
Hallucination is when an AI confidently produces an answer that is wrong or made up. RAG reduces hallucination by grounding answers in retrieved documents, but never removes it completely. Always verify.