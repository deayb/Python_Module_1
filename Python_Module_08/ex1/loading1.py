import sys

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
        print(f"[OK] numpy ({pandas.__version__}) - Numerical computation ready")
    except ModuleNotFoundError:
        status["numpy"] = None
        print("[MISSING] numpy - install with: pip install numpy")

    try:
        import matplotlib
        status["matplotlib"] = matplotlib.__version__
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
    except ModuleNotFoundError:
        status["matplotlib"] = None
        print("[MISSING] matplotlib - install with: pip install matplotlib")

    return status

def generate_matrix_data(n: int = 1000, seed: int = 42):
    import numpy
    rng = numpy.random.default.rng(seed)
    data = rng.normal(loc=50, scale=15, size=n)
    return (data)


def analyse_matrix_data(data):
    import pandas

    print("\nAnalyzing matrix data...")
    print(f"Processing {len(data)} data points...")

    df = pandas.DataFrame({"signal": data})
    stats = df["signal"].describe()

    print("\nStatistics:")
    print(stats)

    return df


def visualize_matrix_data(df) -> None:
    import matplotlib.pyplot as plt

    print("Generating visualization...")

    plt.figure(figsize=(8, 5))
    plt.hist(df["signal"], bins=30, color="green", edgecolor="black")
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal value")
    plt.ylabel("Frequency")

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Result saved to: matrix_analysis.png")



def compare_dependency_management(status: dict[str, str | None]) -> None:
    print("\nDependency management comparison:")
    print("-" * 50)

    for name, ver in status.items():
        if ver is not None:
            print(f"{name:12s} -> installed version: {ver}")
        else:
            print(f"{name:12s} -> not installed")

    print("\npip (requirements.txt):")
    print("  - Flat list of packages, e.g. 'pandas>=2.0.0'")
    print("  - No automatic lock file: two installs can silently")
    print("    resolve to different sub-dependency versions")

    print("\nPoetry (pyproject.toml):")
    print("  - Declares dependencies with version constraints")
    print("  - Resolves the full dependency graph and writes")
    print("    poetry.lock, so every install is reproducible")
    print("  - Manages the virtual environment for you automatically")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    status = check_dependencies()

    required = ["pandas", "numpy", "matplotlib"]
    missing = [name for name in required if status[name] is None]

    if missing:
        print(f"\nERROR: Missing required dependencies: {', '.join(missing)}")
        print("Install with:")
        print("  pip install -r requirements.txt")
        print("  #or")
        print("  poetry install")
        return

    data = generate_matrix_data()
    df = analyse_matrix_data(data)
    visualize_matrix_data(df)
    compare_dependency_management(status)

if __name__ == "__main__":
    main()