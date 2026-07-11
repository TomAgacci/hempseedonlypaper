#!/usr/bin/env python3
"""
Hemp-Seed-Only Paper Mix Definition
(No hemp fibers — seed powder + heated seed oil + lime micro-binder)

This script defines:
- The seed-only paper mix
- Additive preparation
- Tama-style deduction logic
- Final printed recipe
"""

def seed_only_paper_mix():
    """
    Defines the hemp-seed-only paper composite.
    All percentages are fractions of total solids.
    """
    return {
        "Name": "Hemp-Seed-Only Paper",
        "Type": "Seed Resin Sheet",

        # Core solids
        "Seed_powder_frac": 0.70,      # 70% crushed hemp seed micro-powder
        "Lime_frac": 0.05,             # 5% hydrated lime micro-binder

        # Binder system
        "Heated_seed_oil_frac": 0.12,  # 12% polymerizing hemp seed oil
        "Water_ratio": 2.50,           # slurry water ratio (per binder mass)

        # Additives (prepared separately)
        "Additives": {
            "Lecithin_frac": 0.005,    # emulsifier
            "Glycerol_frac": 0.005,    # flexibility
            "Citric_acid_frac": 0.002  # cross-link catalyst
        },

        # Physical properties (estimated)
        "Density_kg_m3": 350,
        "Flexural_MPa": 1.0,
        "Compressive_MPa": 0.3
    }


def tama_deduction_explanation():
    """
    Returns the Tama Quantitative Engine deduction logic
    for converting seedcrete → plywood → seed-paper.
    """
    return (
        "Tama Deduction:\n"
        "- Remove sand entirely\n"
        "- Remove metakaolin\n"
        "- Reduce lime to minimal binder (5%)\n"
        "- Increase seed powder to dominant phase (70%)\n"
        "- Increase water for slurry formation (2.5x binder)\n"
        "- Increase seed oil slightly for polymerization (12%)\n"
        "- Add emulsifier + plasticizer + catalyst\n"
        "Result: A flexible seed-resin sheet instead of a mineral composite."
    )


def print_mix(mix):
    print("\n=== Hemp-Seed-Only Paper Mix ===\n")
    print(f"Name: {mix['Name']}")
    print(f"Type: {mix['Type']}\n")

    print("Core Composition (fractions of solids):")
    print(f"  Seed powder fraction       : {mix['Seed_powder_frac']:.2f}")
    print(f"  Lime fraction              : {mix['Lime_frac']:.2f}")
    print(f"  Heated seed oil fraction   : {mix['Heated_seed_oil_frac']:.2f}")
    print(f"  Water ratio (per binder)   : {mix['Water_ratio']:.2f}\n")

    print("Additives:")
    for k, v in mix["Additives"].items():
        print(f"  {k.replace('_',' ').title():<22}: {v:.3f}")

    print("\nEstimated Physical Properties:")
    print(f"  Density (kg/m³)            : {mix['Density_kg_m3']}")
    print(f"  Flexural Strength (MPa)    : {mix['Flexural_MPa']}")
    print(f"  Compressive Strength (MPa) : {mix['Compressive_MPa']}\n")

    print("=== Tama Deduction Logic ===")
    print(tama_deduction_explanation())


if __name__ == "__main__":
    mix = seed_only_paper_mix()
    print_mix(mix)
