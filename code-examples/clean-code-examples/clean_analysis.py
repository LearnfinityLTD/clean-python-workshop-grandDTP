"""
Survey Analysis Script

This script analyzes survey responses to calculate completion metrics
and identify high-performing participants.

Author: Anwar Abdi, Learnfinity
Date: October 2025
"""

import pandas as pd


def load_survey_data(filepath):
    """
    Load survey responses from CSV file.
    
    Parameters
    ----------
    filepath : str
        Path to the CSV file containing survey data
        
    Returns
    -------
    pd.DataFrame
        Survey data with columns: participant_id, score, status
    """
    return pd.read_csv(filepath)


def filter_complete_responses(data):
    """
    Filter to only include completed survey responses.
    
    Parameters
    ----------
    data : pd.DataFrame
        Survey data with 'status' column
        
    Returns
    -------
    pd.DataFrame
        Data with only complete responses
    """
    return data[data['status'] == 'complete']


def calculate_weighted_score(data):
    """
    Calculate weighted scores (score * 2) for all responses.
    
    This applies a 2x multiplier to raw scores as part of our
    weighting methodology for importance.
    
    Parameters
    ----------
    data : pd.DataFrame
        Survey data with 'score' column
        
    Returns
    -------
    pd.DataFrame
        Data with additional 'weighted_score' column
    """
    data = data.copy()  # Don't modify original dataframe
    data['weighted_score'] = data['score'] * 2
    return data


def calculate_mean_weighted_score(data):
    """
    Calculate mean of weighted scores across all responses.
    
    Parameters
    ----------
    data : pd.DataFrame
        Survey data with 'weighted_score' column
        
    Returns
    -------
    float
        Mean weighted score
    """
    return data['weighted_score'].mean()


def count_high_performers(data, threshold=50):
    """
    Count responses above a score threshold.
    
    Parameters
    ----------
    data : pd.DataFrame
        Survey data with 'score' column
    threshold : int, default=50
        Minimum score to be counted as high performer
        
    Returns
    -------
    int
        Number of responses above threshold
    """
    high_performers = data[data['score'] > threshold]
    return len(high_performers)


def get_high_performer_weighted_scores(data, threshold=50):
    """
    Get weighted scores for high-performing participants.
    
    Parameters
    ----------
    data : pd.DataFrame
        Survey data with 'score' and 'weighted_score' columns
    threshold : int, default=50
        Minimum score to be counted as high performer
        
    Returns
    -------
    list
        Weighted scores of high performers
    """
    high_performers = data[data['score'] > threshold]
    return high_performers['weighted_score'].tolist()


def main():
    """
    Main analysis workflow.
    
    Executes the complete survey analysis pipeline:
    1. Load data
    2. Clean data (remove incomplete responses)
    3. Calculate weighted scores
    4. Compute summary statistics
    5. Display results
    """
    # Load raw data
    print("Loading survey data...")
    data = load_survey_data('survey_data.csv')
    print(f"Loaded {len(data)} total responses")
    
    # Clean data
    print("\nCleaning data...")
    data = data.dropna()  # Remove rows with missing values
    data = filter_complete_responses(data)
    print(f"After cleaning: {len(data)} complete responses")
    
    # Transform data
    print("\nCalculating weighted scores...")
    data = calculate_weighted_score(data)
    
    # Analyze
    print("\n" + "="*50)
    print("ANALYSIS RESULTS")
    print("="*50)
    
    mean_score = calculate_mean_weighted_score(data)
    print(f"\nMean weighted score: {mean_score:.2f}")
    
    high_performer_count = count_high_performers(data, threshold=50)
    print(f"High performers (score > 50): {high_performer_count}")
    
    high_performer_scores = get_high_performer_weighted_scores(data, threshold=50)
    if high_performer_scores:
        print(f"High performer weighted scores: {high_performer_scores}")
        print(f"Average high performer weighted score: {sum(high_performer_scores)/len(high_performer_scores):.2f}")
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
