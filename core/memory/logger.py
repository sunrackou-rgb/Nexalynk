import json
from datetime import datetime, timezone
from pathlib import Path

class TrajectoryLogger:
    def __init__(self, log_path="core/memory/trajectories.jsonl"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def log_event(self, agent_name, action, state_metric):
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": agent_name,
            "action": action,
            "metric": state_metric
        }
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[Nexalynk Logger] Logged event for [{agent_name}]")

if __name__ == "__main__":
    logger = TrajectoryLogger()
    logger.log_event("Strategist", "Initialize Global Wave Grid", 0.7071)
