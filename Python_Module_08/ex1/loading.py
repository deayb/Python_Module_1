from typing import Any


def check_dependencies() -> dict[str, str | None]:
    status: dict[str, str | None] = {}

    try:
        import pandas
        status["pandas"] = pandas.__version__
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ModuleNotFoundError:
        status["pandas"] = None
        print("[MISSING] pandas - install with: pip install pandas")

    try:
        import numpy
        status["numpy"] = numpy.__version__
        print(f"[OK] numpy ({numpy.__version__})"
              " - Numerical computation ready")
    except ModuleNotFoundError:
        status["numpy"] = None
        print("[MISSING] numpy - install with: pip install numpy")

    try:
        import matplotlib
        status["matplotlib"] = matplotlib.__version__
        print(f"[OK] matplotlib ({matplotlib.__version__})"
              " - Visualization ready")
    except ModuleNotFoundError:
        status["matplotlib"] = None
        print("[MISSING] matplotlib - install with: pip install matplotlib")

    try:
        import requests
        status["requests"] = requests.__version__
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
    except ModuleNotFoundError:
        status["requests"] = None
        print("[MISSING] requests - install with: pip install requests")

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


def visualize_matrix_data(df: Any) -> Any:
    import matplotlib.pyplot as plt

    print("Generating visualization....")

    plt.figure(figsize=(8, 5))
    plt.hist(df["signal"], bins=30, color="green", edgecolor="black")
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal value")
    plt.ylabel("Frequency")

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Results saved to: matrix_analysis.png")


def compare_dependency_management(status: dict[str, str | None]) -> None:
    print("\nDependency management comparison:")
    print("-" * 50)

    for name, version in status.items():
        if version is not None:
            print(f"{name:12s} -> installed version: {version}")
        else:
            print(f"{name:12s} -> not installed")

    print("\npip (requirements.txt):")
    print("  - Flat list of packages, e.g. 'pandas>=2.0.0'")
    print("  - No automatic lock file: two installs can silently")
    print("    resolve to different sub-dependency versions")
    print("  - You must run 'pip freeze > requirements.txt' yourself")
    print("    to pin exact versions")

    print("\nPoetry (pyproject.toml):")
    print("  - Declares dependencies with version constraints,")
    print("    e.g. pandas = \"^2.0.0\"")
    print("  - Resolves the full dependency graph and writes")
    print("    poetry.lock, so every install is reproducible")
    print("  - Manages the virtual environment for you automatically")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    status = check_dependencies()

    data = generate_matrix_data()
    df = analyze_matrix_data(data)
    visualize_matrix_data(df)

    compare_dependency_management(status)

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()

