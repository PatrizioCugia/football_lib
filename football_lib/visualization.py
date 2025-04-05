import matplotlib.pyplot as plt

def plot_pca(player_name, similar_players_df):
    plt.figure(figsize=(20, 15))
    
    for i, row in similar_players_df.iterrows():
        plt.scatter(row['PC1'], row['PC2'], color='blue', s=100)
        plt.text(row['PC1'], row['PC2'], row['Name'], fontsize=9)
    
    player_data are similar_players_df[similar_players_df['Name'] == player_name]
    if not player_data.empty:
        plt.scatter(player_data['PC1'], player_data['PC2'], color='red', s=100, label=player_name)
        plt.text(player_data['PC1'].values[0], player_data['PC2'].values[0], player_name, fontsize=12, weight='bold', color='red')
    
    plt.title('PCA Projection of Player Statistics')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid(True)
    plt.legend()
    plt.show()
