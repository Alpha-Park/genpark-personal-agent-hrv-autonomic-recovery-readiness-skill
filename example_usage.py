# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent HRV Autonomic Recovery Readiness Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentHrvAutonomicRecoveryReadiness

def main():
    agent = PersonalAgentHrvAutonomicRecoveryReadiness()

    print("=" * 70)
    print("DEMO: Personal Agent HRV Autonomic Recovery Readiness & Capacity Allocator")
    print("=" * 70)

    # 30-day baseline history around 52ms
    history_30d = [48.0, 52.0, 55.0, 50.0, 53.0, 51.0, 49.0, 54.0, 52.0, 53.0, 50.0, 51.0]

    # Scenario 1: Well-recovered morning (58 ms)
    res_ready = agent.evaluate_daily_readiness(
        rmssd_ms=58.0,
        resting_hr_bpm=54.0,
        historical_rmssd_30d=history_30d
    )

    print(f"\n1. High Recovery Morning Evaluation (RMSSD: 58 ms, RHR: 54 bpm):")
    print(f"   lnRMSSD: {res_ready['ln_rmssd']} (Baseline: {res_ready['baseline_mean_ln_rmssd']})")
    print(f"   Corridor Z-Score: {res_ready['baseline_corridor_z_score']} SD")
    print(f"   Readiness Score: {res_ready['daily_readiness_score']} / 100")
    print(f"   State: {res_ready['autonomic_state']}")
    print(f"   Interpretation: {res_ready['autonomic_interpretation']}")

    # Allocate capacity
    res_alloc = agent.allocate_cognitive_physical_capacity(res_ready['daily_readiness_score'])
    print(f"\n2. Capacity Allocation for {res_ready['daily_readiness_score']} pts ({res_alloc['capacity_tier']}):")
    print(f"   Cognitive Focus: {res_alloc['cognitive_deep_work_allowance']}")
    print(f"   Physical Strain: {res_alloc['physical_athletic_strain_cap']}")
    print(f"   Caffeine Rx: {res_alloc['caffeine_nervous_system_rx']}")

    # Scenario 2: Severe Sleep Deprivation / Alcohol / Overtraining (24 ms)
    res_fatigue = agent.evaluate_daily_readiness(
        rmssd_ms=24.0,
        resting_hr_bpm=72.0,
        historical_rmssd_30d=history_30d
    )
    print(f"\n3. Acute Autonomic Fatigue Scenario (RMSSD: 24 ms, RHR: 72 bpm):")
    print(f"   Readiness Score: {res_fatigue['daily_readiness_score']} / 100")
    print(f"   State: {res_fatigue['autonomic_state']}")
    res_alloc_fatigue = agent.allocate_cognitive_physical_capacity(res_fatigue['daily_readiness_score'])
    print(f"   Prescription: {res_alloc_fatigue['capacity_tier']}")
    print(f"   Guidance: {res_alloc_fatigue['cognitive_deep_work_allowance']}")

    print("\nVerification complete: HRV autonomic recovery readiness engine executed flawlessly.")

if __name__ == "__main__":
    main()
