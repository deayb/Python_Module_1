from typing import Any


def check_dependencies() -> dict[str, str | None]:
    status: dict[str, str | None] = {}

    try:
        import pandas
        status["pandas"] = pandas.__version__
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        status["pandas"] = None
        print("[MISSING] pandas - install with: pip install pandas")

    try:
        import numpy
        status["numpy"] = numpy.__version__
        print(f"[OK] numpy ({numpy.__version__}) - "
              f"Numerical computation ready")
    except ImportError:
        status["numpy"] = None
        print("[MISSING] numpy - install with: pip install numpy")

    try:
        import matplotlib
        status["matplotlib"] = matplotlib.__version__
        print(f"[OK] matplotlib ({matplotlib.__version__}) - "
              f"Visualization ready")
    except ImportError:
        status["matplotlib"] = None
        print("[MISSING] matplotlib - install with: pip install matplotlib")

    return status


def generate_matrix_data(n: int = 1000, seed: int = 42) -> Any:
    import numpy
    rng = numpy.random.default_rng(seed)
    data = rng.normal(loc=50, scale=15, size=n)
    return data


def analyze_matrix_data(data: Any) -> Any:
    import pandas
    print("\nAnalyzing matrix data...")
    print(f"Processing {len(data)} data points...")

    df = pandas.DataFrame({"signal": data})
    stats = df["signal"].describe()

    print("\nStatistics:")
    print(stats)

    return df


def visualize_matrix_data(df: Any) -> None:
    import matplotlib.pyplot as plt

    print("Generating visualization...")

    plt.figure()
    plt.hist(df["signal"], bins=30)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal Values")
    plt.ylabel("Count")
    plt.savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")


def compare_dependency_management(status: dict) -> None:
    print("\nDependency management comparison:")

    for name, ver in status.items():
        if ver is not None:
            print(f"{name} {ver}")
        else:
            print(f"{name}: not installed")

    print("\npip (requirements.txt):")
    print("  - Flat list of packages, e.g. 'pandas>=2.0.0'")
    print("  - You must create and manage the venv yourself")
    print("  - No automatic resolution of sub-dependency conflicts")

    print("\nPoetry (pyproject.toml):")
    print("  - Declares dependencies with version constraints")
    print("  - Automatically resolves the full dependency graph")
    print("  - Manages the virtual environment for you")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    result = check_dependencies()

    missing = []
    for name, ver in result.items():
        if ver is None:
            missing.append(name)

    if missing:
        print(f"ERROR: Missing required dependencies: {', '.join(missing)}")
        print("Install with:")
        print("  pip install -r requirements.txt")
        print("  # or")
        print("  poetry install")
        return
    else:
        print("Everything is good, we can continue.")

    data = generate_matrix_data()
    df = analyze_matrix_data(data)
    visualize_matrix_data(df)
    compare_dependency_management(result)

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
