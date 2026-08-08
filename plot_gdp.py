import matplotlib.pyplot as plt
import os

# Data
years = [2026, 2050]
india_gdp = [2813, 36673]
china_gdp = [14874, 64218]
us_gdp = [85400, 237081]

plt.figure(figsize=(10, 6))
plt.plot(years, india_gdp, marker='o', label='India', color='green', linewidth=2)
plt.plot(years, china_gdp, marker='o', label='China', color='orange', linewidth=2)
plt.plot(years, us_gdp, marker='o', label='United States', color='blue', linewidth=2)

# Annotations
for i, txt in enumerate(india_gdp):
    plt.annotate(f"${txt:,}", (years[i], india_gdp[i]), textcoords="offset points", xytext=(0,-15), ha='center')

for i, txt in enumerate(china_gdp):
    plt.annotate(f"${txt:,}", (years[i], china_gdp[i]), textcoords="offset points", xytext=(0,-15), ha='center')

for i, txt in enumerate(us_gdp):
    plt.annotate(f"${txt:,}", (years[i], us_gdp[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Double headed arrows for the gap (India - US)
plt.annotate('', xy=(2026-0.5, india_gdp[0]), xytext=(2026-0.5, us_gdp[0]),
             arrowprops=dict(arrowstyle='<->', color='red', lw=1.5, ls=':'))
gap_2026_multi_ind = us_gdp[0] / india_gdp[0]
plt.text(2026-2.5, (us_gdp[0] + india_gdp[0])/2.5, f"IN-US Gap: {gap_2026_multi_ind:.1f}x", color='red', va='center')

plt.annotate('', xy=(2050-0.5, india_gdp[1]), xytext=(2050-0.5, us_gdp[1]),
             arrowprops=dict(arrowstyle='<->', color='red', lw=1.5, ls=':'))
gap_2050_multi_ind = us_gdp[1] / india_gdp[1]
plt.text(2050-0.5, (us_gdp[1] + india_gdp[1])/2.5, f"IN-US Gap: {gap_2050_multi_ind:.1f}x", color='red', va='center', ha='right')

# Double headed arrows for the gap (China - US)
plt.annotate('', xy=(2026+0.5, china_gdp[0]), xytext=(2026+0.5, us_gdp[0]),
             arrowprops=dict(arrowstyle='<->', color='orange', lw=1.5, ls=':'))
gap_2026_multi_chn = us_gdp[0] / china_gdp[0]
plt.text(2026+0.5, (us_gdp[0] + china_gdp[0])/1.3, f"CN-US Gap: {gap_2026_multi_chn:.1f}x", color='orange', va='center')

plt.annotate('', xy=(2050+0.5, china_gdp[1]), xytext=(2050+0.5, us_gdp[1]),
             arrowprops=dict(arrowstyle='<->', color='orange', lw=1.5, ls=':'))
gap_2050_multi_chn = us_gdp[1] / china_gdp[1]
plt.text(2050+0.5, (us_gdp[1] + china_gdp[1])/1.3, f"CN-US Gap: {gap_2050_multi_chn:.1f}x", color='orange', va='center', ha='right')

plt.title("India vs China vs US Nominal GDP Per Capita Projections (2026 vs 2050)")
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
