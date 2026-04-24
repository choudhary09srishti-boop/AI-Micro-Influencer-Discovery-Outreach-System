import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

steps = [
    (5, 9.2, "1. USER INPUT", "Brand keyword (e.g., skincare)", "#4A90D9"),
    (5, 7.8, "2. DISCOVERY", "YouTube Data API v3 → Search Indian creators", "#5BA85A"),
    (5, 6.4, "3. FILTERING", "5K–100K subscribers | Country: IN | Recent activity", "#E8A838"),
    (5, 5.0, "4. ENRICHMENT", "Name, Subs, Views, Profile Link, Description", "#9B59B6"),
    (5, 3.6, "5. CONTENT ANALYSIS", "Groq LLM → Niche, Tone, Topics, Engagement", "#E74C3C"),
    (5, 2.2, "6. BRAND MATCHING", "Groq LLM → Relevance Score + Reason", "#1ABC9C"),
    (5, 0.8, "7. OUTREACH GENERATION", "Groq LLM → Personalized Email + Instagram DM", "#E67E22"),
]

for x, y, title, desc, color in steps:
    ax.add_patch(mpatches.FancyBboxPatch((1.2, y-0.45), 7.6, 0.85,
        boxstyle="round,pad=0.1", facecolor=color, edgecolor="white", linewidth=2))
    ax.text(x, y+0.15, title, ha='center', va='center',
        fontsize=11, fontweight='bold', color='white')
    ax.text(x, y-0.18, desc, ha='center', va='center',
        fontsize=8.5, color='white')

for i in range(len(steps)-1):
    y_start = steps[i][1] - 0.45
    y_end = steps[i+1][1] + 0.45
    ax.annotate('', xy=(5, y_end), xytext=(5, y_start),
        arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

ax.text(5, 9.82, "🤖 Automated Micro-Influencer Outreach System",
    ha='center', fontsize=14, fontweight='bold', color='#2C3E50')

plt.tight_layout()
plt.savefig("data/architecture_diagram.png", dpi=150, bbox_inches='tight')
print("✅ Saved to data/architecture_diagram.png")