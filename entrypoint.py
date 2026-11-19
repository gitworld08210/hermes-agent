import os
import sys

# 1. Synchronize Render's dynamic PORT with Hermes API Server
render_port = os.getenv("PORT", "10000")
os.environ["API_SERVER_PORT"] = render_port
os.environ["API_SERVER_HOST"] = "0.0.0.0"

# 2. Ensure a valid, strong API_SERVER_KEY exists (minimum 16 characters required by Hermes)
existing_key = os.getenv("API_SERVER_KEY", "").strip()
if len(existing_key) < 16:
    default_key = "hydrogen_agent_brain_secret_2026_xyz987"
    os.environ["API_SERVER_KEY"] = default_key
    print(f"[*] Using default secure API_SERVER_KEY: {default_key}")
else:
    print("[*] Custom API_SERVER_KEY configured from environment.")

# 3. Enable CORS for cross-origin client access
os.environ.setdefault("API_SERVER_CORS_ORIGINS", "*")

# 4. Disable interactive questions / prompts
os.environ["HERMES_NONINTERACTIVE"] = "1"
os.environ["PYTHONUNBUFFERED"] = "1"

print(f"[*] Starting Hermes Agent API Server on 0.0.0.0:{render_port} ...")

# 5. Launch Hermes Gateway runner
if __name__ == "__main__":
    from gateway.run import main
    main()
