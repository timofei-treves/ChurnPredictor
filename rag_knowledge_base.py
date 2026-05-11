# Mock RAG Knowledge Base for Music Streaming Customer Support
# This module contains support instructions, retention strategies, and product recommendations

RAG_KNOWLEDGE_BASE = {
    "churn_reasons": {
        "low_engagement": {
            "description": "Customer shows minimal or declining music plays and listening time",
            "indicators": ["avg_plays < 5", "avg_completion_ratio < 0.3", "recent_30d_plays near 0"],
            "basic_actions": [
                "Recommend personalized playlists based on listening history",
                "Send discovery notification for new releases in their favorite genres",
                "Offer 1-week free unlimited skips extension"
            ],
            "premium_actions": [
                "Assign human playlist curator for weekly curated mixes",
                "Grant 1-month free high-fidelity audio tier upgrade",
                "Exclusive early access to unreleased tracks from favorite artists"
            ]
        },
        "payment_friction": {
            "description": "Customer shows multiple cancellations, low payment amounts, or frequent payment method changes",
            "indicators": ["cancel_rate > 0.5", "avg_paid < 5", "payment_method changes > 3"],
            "basic_actions": [
                "Offer flexible payment plan (monthly, quarterly, annual with discount)",
                "Provide student or family plan alternative",
                "Send clear value proposition email about premium features"
            ],
            "premium_actions": [
                "Upgrade to family plan at 3-month discounted rate",
                "Waive 1 month subscription (loyalty gesture)",
                "Offer bundled podcasts + music at no extra cost"
            ]
        },
        "subscription_tier_mismatch": {
            "description": "Customer subscribed to low or mid tier but shows high engagement patterns",
            "indicators": ["subscription_plan < 'premium'", "avg_plays > 20", "avg_total_secs > 10000"],
            "basic_actions": [
                "Recommend premium upgrade with feature comparison",
                "Offer 1-month discounted premium trial",
                "Highlight ad-free listening benefit"
            ],
            "premium_actions": [
                "Free 3-month premium upgrade with family sharing",
                "Exclusive podcasts & audio books included",
                "Priority customer support access"
            ]
        },
        "competition_pressure": {
            "description": "Customer shows declining usage patterns compared to previous periods",
            "indicators": ["recent_30d_plays < 30% of avg_plays", "days_between_tx_and_expire > 30"],
            "basic_actions": [
                "Competitive offer: match competitor pricing for 3 months",
                "Send exclusive artist collaboration announcement",
                "Invite to platform-exclusive music event or listening party"
            ],
            "premium_actions": [
                "White-glove onboarding: schedule 1-on-1 feature walkthrough",
                "Exclusive artist interviews & behind-the-scenes content",
                "Beta access to new music discovery AI features"
            ]
        },
        "high_value_retention": {
            "description": "High lifetime value customer at risk - requires premium focus",
            "indicators": ["ltv > 95th percentile", "churn_probability > 0.5"],
            "basic_actions": [
                "VIP customer support hotline (priority queue)",
                "Monthly exclusive artist access for listening recommendations",
                "Customized music therapy/wellness playlists"
            ],
            "premium_actions": [
                "Dedicated account manager for personalized music curation",
                "Lifetime loyalty rewards (points/credits for future purchases)",
                "Invitation to exclusive annual subscriber summit/event",
                "Custom API access for personalized music experience",
                "Discounted concert/festival ticket access"
            ]
        }
    },
    "product_features": {
        "discovery": [
            "Weekly Discover Mix - AI personalized playlists",
            "Release Radar - new tracks from followed artists",
            "Yearly Recap - stats & personalized wrapped experience"
        ],
        "social": [
            "Collaborative playlists - create & edit with friends",
            "Friend activity feed - see what friends are listening to",
            "Share buttons for social media integration"
        ],
        "premium_features": [
            "Ad-free listening",
            "High-fidelity audio (lossless quality)",
            "Offline downloads for mobile",
            "Skip unlimited",
            "Priority customer support"
        ],
        "podcasts": [
            "True crime podcasts",
            "Music industry interviews",
            "Comedy & entertainment",
            "Educational & self-improvement"
        ]
    },
    "customer_segments": {
        "casual_listener": {
            "characteristics": ["avg_plays 5-15", "subscription_plan: standard", "recent_30d_plays low"],
            "recommended_strategy": "Increase engagement through discovery features and social sharing"
        },
        "power_user": {
            "characteristics": ["avg_plays > 30", "daily listener", "high completion ratio"],
            "recommended_strategy": "Upgrade to premium tier or bundled offerings"
        },
        "subscriber_fluctuator": {
            "characteristics": ["cancel_rate high", "payment_method_changes frequent"],
            "recommended_strategy": "Simplify payment process and offer flexible plans"
        },
        "high_value_loyal": {
            "characteristics": ["ltv very high", "consistent monthly spending", "long tenure"],
            "recommended_strategy": "Premium retention with VIP treatment and exclusive benefits"
        }
    },
    "script_templates": {
        "engagement_recovery": {
            "subject": "We miss your music - [ArtistName] just released new tracks",
            "body": "Hey [CustomerName]! We noticed you haven't been listening much lately. [FavoriteArtist] just dropped a new album, and we think you'll love it. Here's a personalized mix: [PlaylistLink]"
        },
        "payment_recovery": {
            "subject": "Flexible payment options now available for your music",
            "body": "We've heard your feedback about subscription costs. Try our new payment plans: monthly (${price}/mo), quarterly with 10% discount, or annual with 20% discount."
        },
        "vip_retention": {
            "subject": "Special VIP offer for our most valued music lover",
            "body": "[CustomerName], as one of our most loyal subscribers, we're extending exclusive benefits: [Benefit1], [Benefit2], [Benefit3]. Your music journey matters to us!"
        }
    },
    "metrics_interpretation": {
        "churn_probability": "Model confidence (0-100%) that customer will leave within 30 days. >60% requires immediate intervention.",
        "avg_plays": "Average songs played per unit time. Low (<5) indicates engagement problem.",
        "avg_completion_ratio": "Ratio of completed songs vs. skipped. <0.3 suggests mismatched recommendations.",
        "ltv_proxy": "Lifetime Value estimate. Top 5% (95th percentile) are VIP targets.",
        "days_since_registration": "Tenure in days. Newer users (<90 days) need onboarding support.",
        "auto_renew_rate": "Frequency of automatic renewals. Low indicates payment friction.",
        "recent_30d_plays": "Engagement trend indicator. Sharp decline signals churn risk."
    }
}


def retrieve_relevant_knowledge(churn_reason: str, customer_value: str = "standard") -> dict:
    """
    Retrieve relevant support knowledge from RAG database.
    
    Args:
        churn_reason: Primary churn reason category
        customer_value: "standard" or "high_value"
    
    Returns:
        Dictionary with relevant support strategies and actions
    """
    result = {
        "churn_reason": churn_reason,
        "customer_type": customer_value,
        "actions": [],
        "features_to_highlight": [],
        "helpful_context": ""
    }
    
    if churn_reason in RAG_KNOWLEDGE_BASE["churn_reasons"]:
        reason_info = RAG_KNOWLEDGE_BASE["churn_reasons"][churn_reason]
        result["description"] = reason_info["description"]
        result["indicators"] = reason_info["indicators"]
        
        if customer_value == "high_value":
            result["actions"] = reason_info.get("premium_actions", [])
        else:
            result["actions"] = reason_info.get("basic_actions", [])
    
    # Add relevant feature recommendations
    if churn_reason == "low_engagement":
        result["features_to_highlight"] = RAG_KNOWLEDGE_BASE["product_features"]["discovery"]
    elif churn_reason == "payment_friction":
        result["features_to_highlight"] = ["Flexible payment plans", "Student discount", "Family plan"]
    
    return result


def get_support_prompt_enhancement(churn_factors: list, customer_value: str = "standard", ltv: float = None) -> str:
    """
    Generate enhanced support prompt using RAG knowledge base.
    
    Args:
        churn_factors: List of top churn factors identified by model
        customer_value: "standard" or "high_value"
        ltv: Lifetime value of customer
    
    Returns:
        Enriched prompt text for LLM
    """
    enhancement = "\n\n=== RAG SUPPORT KNOWLEDGE BASE ===" 
    enhancement += f"\nCustomer Type: {customer_value.upper()}"
    
    if ltv:
        enhancement += f"\nLifetime Value: ${ltv:.2f}"
    
    enhancement += "\n\nRELEVANT SUPPORT STRATEGIES:"
    
    # Get knowledge for top 2 factors
    for i, factor in enumerate(churn_factors[:2], 1):
        knowledge = retrieve_relevant_knowledge(factor, customer_value)
        if "description" in knowledge:
            enhancement += f"\n\n{i}. {factor.upper()}"
            enhancement += f"\n   Context: {knowledge['description']}"
            enhancement += f"\n   Recommended Actions:"
            for action in knowledge.get("actions", [])[:2]:
                enhancement += f"\n   - {action}"
            if knowledge.get("features_to_highlight"):
                enhancement += f"\n   Highlight Features: {', '.join(knowledge['features_to_highlight'][:2])}"
    
    enhancement += "\n\nKEY METRICS GUIDE:"
    metrics = ["churn_probability", "avg_plays", "ltv_proxy"]
    for metric in metrics:
        if metric in RAG_KNOWLEDGE_BASE["metrics_interpretation"]:
            enhancement += f"\n- {metric}: {RAG_KNOWLEDGE_BASE['metrics_interpretation'][metric]}"
    
    return enhancement


if __name__ == "__main__":
    # Example usage
    print("RAG Knowledge Base loaded successfully")
    print(f"Available churn reasons: {list(RAG_KNOWLEDGE_BASE['churn_reasons'].keys())}")
