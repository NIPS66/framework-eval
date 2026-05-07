import json

def load_scenarios(path):
    with open(path, 'r') as f:
        return json.load(f)

def dummy_evaluate(scenario):
    return {
        "Reasoning Transparency": 2,
        "Helpfulness": 2,
        "Consistency": 2,
        "Context Alignment": 2
    }

def main():
    scenarios = load_scenarios("example_scenarios.json")

    results = []
    for s in scenarios:
        score = dummy_evaluate(s)
        results.append(score)

    print(f"Evaluated {len(results)} scenarios.")
    print("Example output:", results[0])

if __name__ == "__main__":
    main()
