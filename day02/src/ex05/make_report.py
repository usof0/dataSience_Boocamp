import sys
from config import NUM_OF_STEPS, REPORT
from analytics import Research

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python3 first_nest.py <file_path>")
        file_path = sys.argv[1]

        research = Research(file_path)

        has_header = research.has_header()
        data = research.file_reader(has_header)
        heads, tails = research.Analytics.counts(data)
        head_fraction, tail_fraction = research.Analytics.fractions(heads, tails)
        
        predictions = research.Analytics.predict_random(NUM_OF_STEPS)

        predicted_heads, predicted_tails = research.Analytics.counts(predictions)

        report =  REPORT.format(
            observations = len(data),
            heads = heads,
            tails = tails,
            tail_fraction = tail_fraction,
            head_fraction = head_fraction,
            predictions = len(predictions),
            predicted_heads = predicted_heads,
            predicted_tails = predicted_tails
        )

        research.Analytics.save_file(report, 'report.txt')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
