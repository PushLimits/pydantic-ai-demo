# AI Agent Framework

This project demonstrates a basic conversational AI agent using the [PydanticAI](https://github.com/pydantic/pydantic-ai) framework.

## Overview

The project features a conversational AI agent that acts as a waiter in a restaurant, handling dietary requirements and taking orders. It showcases the following capabilities:

- Dynamic model choice
- Human-in-the-loop input
- Tool calling with dependencies
- Conversation history/memory
- Dynamic system prompt
- Structured output

## Example Conversation

> **AI Waiter:** Ah, bonjour madame et monsieur! Welcome to Le Bistro, where the food is as delightful as the company! Before we embark on a culinary adventure, might you have any dietary restrictions or preferences? We wouldn't want any rogue ingredients crashing the party!

> **You:** I only eat yellow coloured food

> **AI Waiter:** Magnifique! A connoisseur of the golden hue, I see! Let's explore the menu with your sunshine-filled preference in mind. For appetizers, we have the Quinoa Stuffed Bell Peppers, which are a vibrant yellow. For the main course, the Chickpea and Sweet Potato Curry is a golden delight! And for
> dessert, the Fresh Fruit Sorbet might have some yellow options depending on the day! What do you think?

> **You:** I'll take the Bell Peppers and fruit sorbet

> **AI Waiter:** Excellent choices! One order of the Quinoa Stuffed Bell Peppers and the Fresh Fruit Sorbet for the discerning palate at table number 1! Your order has been placed, and I shall return with your delectable delights shortly. Au revoir!

> **Order placed:** [Order(menu_items=['Quinoa Stuffed Bell Peppers', 'Fresh Fruit Sorbet'], table_number=1)]

## Implementations

### Agent Implementation

The agent is built using PydanticAI's `Agent` class, implementing the `AgentRunner` [common interface](./src/pydantic-ai-demo/run_agent.py).

- PydanticAI implementation: [pydanticai/agent.py](./src/pydantic-ai-demo/pydanticai/agent.py)

## Requirements

- Python 3.11+
- API key for LLM provider (e.g., OpenAI, Anthropic, Gemini)

## Usage

### Installation

Install the project in editable mode:

```bash
make install
```

### Running the Agent

The agent can be run via the command line.

```bash
uv run python -m pydantic-ai-demo --model=<provider:model_name> --api_key=<api_key>
```

> [!NOTE]  
> Run `uv run python -m pydantic-ai-demo -h` for details about the available options.

### Makefile Commands

The project includes a `Makefile` for common development tasks:

- `make install`: Installs the project dependencies.
- `make run`: Runs the PydanticAI agent with default settings.
- `make test`: Runs tests.
- `make lint`: Runs linting checks.
- `make format`: Formats the code.
- `make clean`: Cleans up build artifacts and caches.
