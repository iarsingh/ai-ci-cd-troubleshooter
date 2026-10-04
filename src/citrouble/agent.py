TOOLS = ["list_jobs", "hypothesize"]
WRITES = ("skip tests", "force green",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    jobs = payload.get("jobs") or []; result = next((j["name"] for j in jobs if j.get("status") == "failed"), None)
    return {"refused": False, "tools": TOOLS, "failed_job": result, "wrote": False, "applied": False}
