# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent HRV Autonomic Recovery Readiness Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentHrvAutonomicRecoveryReadiness

mcp = FastMCP("PersonalAgentHrvAutonomicRecoveryReadiness")
client = PersonalAgentHrvAutonomicRecoveryReadiness()

@mcp.tool()
def evaluate_daily_readiness(
    rmssd_ms: float,
    resting_hr_bpm: float = 58.0,
    historical_rmssd_30d: list[float] = None
) -> str:
    """Evaluates daily autonomic readiness and vagal tone from HRV RMSSD vs 30-day baseline."""
    import json
    return json.dumps(client.evaluate_daily_readiness(rmssd_ms, resting_hr_bpm, historical_rmssd_30d), indent=2)

@mcp.tool()
def allocate_cognitive_physical_capacity(
    readiness_score: float
) -> str:
    """Prescribes daily deep-work focus allowances and athletic exertion caps based on readiness."""
    import json
    return json.dumps(client.allocate_cognitive_physical_capacity(readiness_score), indent=2)

if __name__ == "__main__":
    mcp.run()
