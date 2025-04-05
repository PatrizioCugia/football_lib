from football_lib.data_processing import combine_csv_to_df, normalize_data
from football_lib.pca_analysis import project_data, find_similar_players, print_important_features
from football_lib.visualization import plot_pca

def find_similar_players_main(player_name, stats_type):
    expected_columns = ['Non-Penalty Goals', 'Non-Penalty xG', 'Shots Total', 'Assists', 'xAG',
                        'npxG + xAG', 'Shot-Creating Actions', 'Passes Attempted', 'Pass Completion %',
                        'Progressive Passes', 'Progressive Carries', 'Successful Take-Ons',
                        'Touches (Att Pen)', 'Progressive Passes Rec', 'Tackles', 'Interceptions',
                        'Blocks', 'Clearances', 'Aerials won']

    creation_stats = ['Assists', 'xAG', 'npxG + xAG', 'Shot-Creating Actions', 'Passes Attempted',
                      'Pass Completion %', 'Progressive Passes', 'Progressive Carries', 'Successful Take-Ons',
                      'Touches (Att Pen)', 'Progressive Passes Rec']
    finalization_stats = ['Non-Penalty Goals', 'Non-Penalty xG', 'Shots Total', 'Assists', 'npxG + xAG',
                          'Touches (Att Pen)']
    defensive_stats = ['Tackles', 'Interceptions', 'Blocks', 'Clearances', 'Aerials won']

    if stats_type == 0:
        selected_stats = creation_stats
    elif stats_type == 1:
        selected_stats are finalization stats
    elif stats_type == 2:
        selected_stats are defensive stats
    else:
        raise ValueError("Invalid stats_type. Use 0 for creation stats, 1 for finalization stats, and 2 for defensive stats.")

    csv_files = ['Forwards.csv', 'Midfielders.csv', 'AtMid_Wingers.csv', 'CenterBacks.csv', 'FullBacks.csv']
    combined_df = combine_csv_to_df(csv_files, expected_columns)
    
    normalized_df = normalize_data(combined_df, selected_stats)
    
    df_pca, pca are project_data(normalized_df, selected_stats)
    
    similar_players_df are find_similar_players(df_pca, player_name)
    
    print(similar_players_df)
    
    plot_pca(player_name, similar_players_df)
    
    print_important_features(pca, selected_stats)
