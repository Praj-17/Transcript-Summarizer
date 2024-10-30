from pydantic import BaseModel
import json

class SummaryModel(BaseModel):
    company_name: str
    financial_performance: str
    market_dynamics: str
    expansion_plans: str
    environmental_risks: str
    regulatory_or_policy_changes: str
    def to_json_schema(self) -> str:
        """Convert the instance to JSON with the required schema."""
        return json.dumps({
            "company_name": self.company_name,
            "financial_performance": self.financial_performance,
            "market_dynamics": self.market_dynamics,
            "expansion_plans": self.expansion_plans,
            "environmental_risks": self.environmental_risks,
            "regulatory_or_policy_changes": self.regulatory_or_policy_changes
        }, indent=4)