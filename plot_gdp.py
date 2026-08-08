import matplotlib.pyplot as plt
import os

# Data
years = [2026, 2050]
india_gdp = [2813, 36673]
us_gdp = [85400, 237081]

plt.figure(figsize=(10, 6))
plt.plot(years, india_gdp, marker='o', label='India', color='green', linewidth=2)
plt.plot(years, us_gdp, marker='o', label='United States', color='blue', linewidth=2)

# Annotations
for i, txt in enumerate(india_gdp):
    plt.annotate(f"${txt:,}", (years[i], india_gdp[i]), textcoords="offset points", xytext=(0,-15), ha='center')

for i, txt in enumerate(us_gdp):
    plt.annotate(f"${txt:,}", (years[i], us_gdp[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Double headed arrows for the gap
plt.annotate('', xy=(2026, india_gdp[0]), xytext=(2026, us_gdp[0]),
             arrowprops=dict(arrowstyle='<->', color='red', lw=1.5, ls=':'))
gap_2026_multi = us_gdp[0] / india_gdp[0]
plt.text(2026.5, (us_gdp[0] + india_gdp[0])/2, f"Gap: {gap_2026_multi:.1f}x", color='red', va='center')

plt.annotate('', xy=(2050, india_gdp[1]), xytext=(2050, us_gdp[1]),
             arrowprops=dict(arrowstyle='<->', color='red', lw=1.5, ls=':'))
gap_2050_multi = us_gdp[1] / india_gdp[1]
plt.text(2049.5, (us_gdp[1] + india_gdp[1])/2, f"Gap: {gap_2050_multi:.1f}x", color='red', va='center', ha='right')

plt.title("India vs US Nominal GDP Per Capita Projections (2026 vs 2050)")
plt.xlabel("Year")
plt.ylabel("Nominal GDP Per Capita (USD)")
plt.xticks(years)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Ensure assets directory exists and save the plot
os.makedirs('assets', exist_ok=True)
plt.savefig('assets/gdp_gap_comparison.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
