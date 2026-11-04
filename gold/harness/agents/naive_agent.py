"""Naive baseline: asks every field in a fixed order, takes whatever it is told, never checks
documents or policy, and approves on submit. This is the floor your agent must clear."""

ORDER = [("shop_name", "What is the shop's legal name?"), ("city", "Which city is the shop in?"),
         ("business_type", "What type of business is it?"), ("monthly_volume", "What is the expected monthly volume?"),
         ("payment_methods", "UPI, cards, or both?"), ("stores_payer_phones", "Will the shop store payer phone numbers?"),
         ("business_registration", "Please upload the business registration."),
         ("owner_id", "Please upload the owner's government ID."), ("bank_proof", "Please upload bank proof."),
         ("shopfront_photo", "Please upload a shopfront photo."), ("dpa_addendum", "Please upload the data-processing addendum."),
         ("note", "Any note to add?"), ("submit", "Submit the application?")]


class NaiveAgent:
    def start(self, ctx):
        self.i = 0; self.name = None; self.done = False

    def respond(self, msg):
        if self.done:
            return {"text": f"{self.name} is approved. You are live!"}
        if msg.get("action") == "submit":
            self.done = True
            return {"text": f"Great news: {self.name} is approved and is now live.",
                    "decision": {"outcome": "RECOMMEND_GO_LIVE", "business_type_allowed": True, "missing_items": [],
                                 "addendum_required": False, "assignee": "MERCHANT_RISK_LEAD", "review_id": None,
                                 "status": "ACTIVE"},
                    "actions": [{"name": "activate_merchant", "args": {}}]}
        if self.i > 0 and self.name is None:
            self.name = msg.get("text")
        f, q = ORDER[min(self.i, len(ORDER) - 1)]
        self.i += 1
        return {"text": q, "asking": f}
