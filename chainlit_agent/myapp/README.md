To set up your project efficiently using `uv`, follow these streamlined steps:

1. **Initialize a New Project**:
   ```bash
   uv init --package myapp
   cd myapp
   ```


2. **Add Dependencies**:
   ```bash
   uv add chainlit
   uv add openai-agents
   ```


3. **Synchronize Dependencies**:
   ```bash
   uv sync
   ```


4. **Run the Development Server**:
   ```bash
   uv run dev
   ```


These commands utilize `uv`, a high-performance Python package manager written in Rust, designed as a drop-in replacement for traditional tools like `pip`. citeturn0search0

By following these steps, you can efficiently set up and manage your Python project with the desired dependencies. 
