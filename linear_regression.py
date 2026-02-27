"""
Simple Linear Regression Coefficients Calculator
=================================================
Calculate β₀ (intercept) and β₁ (slope) for simple linear regression.

Model: Y = β₀ + β₁ * X

Formulas:
    β₁ = Σ((Xᵢ - X̄)(Yᵢ - Ȳ)) / Σ((Xᵢ - X̄)²)
    β₀ = Ȳ - β₁ * X̄
"""


def calculate_regression_coefficients(X, Y):
    """Calculate simple linear regression coefficients β₀ and β₁.

    Args:
        X (list): List of independent variable values (must be non-empty).
        Y (list): List of dependent variable values (same length as X).

    Returns:
        tuple: (β₀, β₁) where β₀ is the intercept and β₁ is the slope.

    Raises:
        ValueError: If X or Y are empty, have different lengths, or all X
                    values are identical (zero variance).
    """
    if not X or not Y:
        raise ValueError("X and Y must not be empty.")
    if len(X) != len(Y):
        raise ValueError("X and Y must have the same length.")

    n = len(X)

    # Step 1: Calculate means
    x_mean = sum(X) / n
    y_mean = sum(Y) / n

    print("=" * 50)
    print("Simple Linear Regression Coefficients")
    print("=" * 50)
    print(f"\nData:")
    print(f"  X = {X}")
    print(f"  Y = {Y}")
    print(f"  n = {n}")

    print(f"\nStep 1: Calculate means")
    print(f"  X̄ = ΣXᵢ / n = {sum(X)} / {n} = {x_mean}")
    print(f"  Ȳ = ΣYᵢ / n = {sum(Y)} / {n} = {y_mean}")

    # Step 2: Calculate deviations and products
    print(f"\nStep 2: Calculate deviations (Xᵢ - X̄), (Yᵢ - Ȳ), and products")
    print(f"  {'Xᵢ':>5} {'Yᵢ':>5} {'(Xᵢ-X̄)':>10} {'(Yᵢ-Ȳ)':>10} "
          f"{'(Xᵢ-X̄)(Yᵢ-Ȳ)':>15} {'(Xᵢ-X̄)²':>12}")
    print(f"  {'-'*67}")

    sum_xy = 0.0
    sum_xx = 0.0
    for xi, yi in zip(X, Y):
        dx = xi - x_mean
        dy = yi - y_mean
        xy = dx * dy
        xx = dx ** 2
        sum_xy += xy
        sum_xx += xx
        print(f"  {xi:>5} {yi:>5} {dx:>10.2f} {dy:>10.2f} {xy:>15.2f} {xx:>12.2f}")

    print(f"  {'-'*67}")
    print(f"  {'Σ':>5} {'':>5} {'':>10} {'':>10} {sum_xy:>15.2f} {sum_xx:>12.2f}")

    # Step 3: Calculate β₁
    if sum_xx == 0:
        raise ValueError("All X values are identical; regression slope is undefined.")
    print(f"\nStep 3: Calculate β₁ (slope)")
    print(f"  β₁ = Σ((Xᵢ - X̄)(Yᵢ - Ȳ)) / Σ((Xᵢ - X̄)²)")
    print(f"  β₁ = {sum_xy} / {sum_xx}")
    beta1 = sum_xy / sum_xx
    print(f"  β₁ = {beta1:.4f}")

    # Step 4: Calculate β₀
    print(f"\nStep 4: Calculate β₀ (intercept)")
    print(f"  β₀ = Ȳ - β₁ * X̄")
    print(f"  β₀ = {y_mean} - {beta1:.4f} * {x_mean}")
    beta0 = y_mean - beta1 * x_mean
    print(f"  β₀ = {beta0:.4f}")

    print(f"\n{'=' * 50}")
    print(f"Results:")
    print(f"  β₀ (intercept) = {beta0:.4f}")
    print(f"  β₁ (slope)     = {beta1:.4f}")
    print(f"\nRegression Equation:")
    print(f"  Y = {beta0:.4f} + {beta1:.4f} * X")
    print("=" * 50)

    return beta0, beta1


if __name__ == "__main__":
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]

    beta0, beta1 = calculate_regression_coefficients(X, Y)
