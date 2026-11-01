# -*- coding: utf-8 -*-
"""
Personal Agent HRV Autonomic Recovery Readiness Client
Zero-dependency Heart Rate Variability (HRV) RMSSD/lnRMSSD autonomic nervous system
balance evaluator, 30-day rolling baseline corridor tracker, and daily cognitive/physical
capacity allocation engine.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentHrvAutonomicRecoveryReadiness:
    """
    Evaluates vagal autonomic tone from nocturnal or morning resting HRV RMSSD values,
    tracking personal rolling baseline corridors and allocating daily cognitive and athletic strain.
    """

    def evaluate_daily_readiness(
        self,
        rmssd_ms: float,
        resting_hr_bpm: float = 58.0,
        historical_rmssd_30d: Optional[List[float]] = None
    ) -> Dict[str, Any]:
        """
        Calculates daily autonomic readiness using natural log transformed RMSSD (lnRMSSD)
        relative to individual 30-day rolling mean and standard deviation corridors.
        """
        rmssd = max(8.0, min(220.0, float(rmssd_ms)))
        rhr = max(35.0, min(120.0, float(resting_hr_bpm)))
        ln_rmssd = round(math.log(rmssd), 3)

        # Baseline computation
        if historical_rmssd_30d and len(historical_rmssd_30d) >= 7:
            ln_history = [math.log(max(8.0, min(220.0, float(x)))) for x in historical_rmssd_30d]
            baseline_mean = sum(ln_history) / len(ln_history)
            variance = sum((x - baseline_mean) ** 2 for x in ln_history) / len(ln_history)
            baseline_sd = max(0.08, math.sqrt(variance))
        else:
            # Standard physiological reference baseline if history is sparse
            baseline_mean = math.log(48.0) # ~ 3.87
            baseline_sd = 0.22

        z_score = round((ln_rmssd - baseline_mean) / baseline_sd, 2)

        # Autonomic state classification
        if -0.5 <= z_score <= 0.75:
            state = "Optimal Autonomic Balance (Homeostatic Equilibrium)"
            readiness = round(min(100.0, 90.0 + (z_score * 10.0)), 1)
            description = "Robust vagal tone with balanced parasympathetic-sympathetic modulation. Peak capacity for deep creative synthesis and physical output."
        elif 0.75 < z_score <= 1.5:
            state = "Elevated Parasympathetic Recovery"
            readiness = 88.0
            description = "Restorative rebound. High resilience and calm nervous system."
        elif z_score > 1.5:
            state = "Parasympathetic Hyper-Saturation"
            readiness = 62.0
            description = "Unusually high HRV paired with depressed heart rate can signal central autonomic fatigue or impending systemic crash. Prioritize restorative pacing."
        elif -1.5 <= z_score < -0.5:
            state = "Mild Sympathetic Dominance"
            readiness = round(max(55.0, 75.0 + (z_score * 15.0)), 1)
            description = "Incomplete recovery or acute cognitive/metabolic strain. Reduce peak high-friction demands."
        else:
            state = "Severe Sympathetic Exhaustion / Systemic Strain"
            readiness = round(max(25.0, 45.0 + (z_score * 10.0)), 1)
            description = "Acute vagal withdrawal. Immune, psychological, or physical overtraining stress. Restrict to restorative work and active recovery."

        return {
            "measured_rmssd_ms": rmssd,
            "resting_hr_bpm": rhr,
            "ln_rmssd": ln_rmssd,
            "baseline_mean_ln_rmssd": round(baseline_mean, 3),
            "baseline_corridor_z_score": z_score,
            "autonomic_state": state,
            "daily_readiness_score": readiness,
            "autonomic_interpretation": description
        }

    def allocate_cognitive_physical_capacity(
        self,
        readiness_score: float
    ) -> Dict[str, Any]:
        """
        Prescribes optimal cognitive deep-work session durations, intellectual friction capacity,
        and athletic exertion limits based on the computed readiness score (0-100).
        """
        score = max(0.0, min(100.0, float(readiness_score)))

        if score >= 85.0:
            cognitive_blocks = "Up to 3-4 intense 90-minute deep work blocks (high architectural decisions, mathematical proofs, complex coding)."
            cardio_limit = "Max intensity permitted: VO2max intervals, heavy compound resistance training, high glycolytic load."
            caffeine_strategy = "Standard morning caffeine titration (100-200mg). Stop 10 hours before sleep."
            strain_tier = "PEAK CAPACITY (Full throttle)"
        elif score >= 65.0:
            cognitive_blocks = "2-3 focused 60-90 minute deep work blocks. Reserve remaining time for review and tactical implementation."
            cardio_limit = "Moderate intensity: Zone 2 aerobic base (30-60 min) or moderate hypertrophy training. Avoid reaching muscular failure."
            caffeine_strategy = "Moderate caffeine. Supplement with 200mg L-theanine to avoid sympathetic jitter."
            strain_tier = "MODERATE CAPACITY (Sustained pacing)"
        elif score >= 45.0:
            cognitive_blocks = "1-2 focused 45-minute blocks maximum. Focus predominantly on routine administration, asynchronous messaging, and documentation."
            cardio_limit = "Active recovery only: 45-minute Zone 1 walking, mobility drills, gentle stretching. Zero high-intensity intervals."
            caffeine_strategy = "Limit caffeine to <= 100mg early morning. Avoid late stimulants."
            strain_tier = "CONSERVATIVE CAPACITY (Prioritize preservation)"
        else:
            cognitive_blocks = "Zero heavy decision-making blocks. Mandatory low-cognitive-friction tasks, light inbox pruning, and restorative naps."
            cardio_limit = "Complete physical deload: Leisurely stroll in nature, breathwork, sauna relaxation, restorative sleep."
            caffeine_strategy = "Zero caffeine or decaffeinated herbal infusions only. Support adrenal recovery."
            strain_tier = "CRITICAL RECOVERY (Mandatory down-regulation)"

        return {
            "evaluated_readiness_score": score,
            "capacity_tier": strain_tier,
            "cognitive_deep_work_allowance": cognitive_blocks,
            "physical_athletic_strain_cap": cardio_limit,
            "caffeine_nervous_system_rx": caffeine_strategy
        }
