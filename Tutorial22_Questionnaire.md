{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kunaal-gupta/Air-Draw-Project/blob/main/Tutorial22_Questionnaire.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "3b9715e6",
      "metadata": {
        "id": "3b9715e6"
      },
      "source": [
        "# Introduction"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "7a482ac9",
      "metadata": {
        "id": "7a482ac9"
      },
      "source": [
        "Important Info:\n",
        "\n",
        "Libraries:\n",
        "- You'll want to import libraries such as numpy, pandas, a plotting library like plotly/matplotlib, and a stats library of your choosing (sklearn for example)\n",
        "\n",
        "Data Info:\n",
        "- There are two data files. One has a condensed event set from a randomly chosen hockey game and the other contains Expected Goals values (xg) provided only for shots that successfully hit the net. If an xg value doesn't correspond to a shot event, it should not be counted\n",
        "\n",
        "- X and Y Coordinates are in Feet and are adjusted such that both teams shoot in the same direction\n",
        "\n",
        "- Line Carry events are tagged when the puck is carried over either blue line or the centre ice red line\n",
        "\n",
        "- Binary columns that have values of 0 or 1 indicate 0=No, 1=Yes\n",
        "\n",
        "- Successfull passes are completed passes, successful shots are shots on net\n",
        "\n",
        "Please show all work, keep written answers succinct and to the point and most of all, thanks for your time and good luck!"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "2d0b5ce9",
      "metadata": {
        "id": "2d0b5ce9"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "id": "76a61952",
      "metadata": {
        "id": "76a61952"
      },
      "source": [
        "## Q1) \n",
        "### a) Who won the game & what was the score?\n",
        "### b) Who won the Expected Goals (xg) battle & what was each team's total xg?\n",
        "### c) What do these two answers tell us about how the two teams played?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "cd930532",
      "metadata": {
        "scrolled": true,
        "id": "cd930532",
        "outputId": "eec91068-2fd9-425a-91d2-0b7141fdf9c3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Team 596 won the game, and their score was 4.\n",
            "\n",
            "Team 596.0 has won the Expected goal battle\n",
            "Each team' total expected goal \n",
            "    teamid        xg\n",
            "0     596  0.152988\n",
            "1     724  0.103933\n",
            "\n",
            " Comparing expected goal value & score of the teams, team 596 performed better\n"
          ]
        }
      ],
      "source": [
        "# Importing pandas library as pd\n",
        "import pandas as pd\n",
        "\n",
        "# Reading data from csv files\n",
        "df1 = pd.read_csv('Tutorial22_df.csv')\n",
        "df2 = pd.read_csv('Tutorial22_xG_df.csv')\n",
        "\n",
        "Team = None\n",
        "\n",
        "\n",
        "def part_a():\n",
        "    \"\"\"  Who won the game & what was the score? \"\"\"\n",
        "\n",
        "    global Team  # Declaring global variable for later usage\n",
        "\n",
        "    # Calculating total goal of each team by grouping\n",
        "    ds = df1.groupby(['teamid'], as_index=False)['goal'].sum()\n",
        "\n",
        "    # Storing Team name & its score\n",
        "    Team = ds.loc[ds['goal'].idxmax()].tolist()[0]\n",
        "    Score = ds.loc[ds['goal'].idxmax()].tolist()[1]\n",
        "\n",
        "    print('Team {} won the game, and their score was {}.'.format(Team, Score) + '\\n')\n",
        "\n",
        "\n",
        "def part_b():\n",
        "    \"\"\" Who won the Expected Goals (xg) battle & what was each team's total xg? \"\"\"\n",
        "\n",
        "    # Calculating the expected goal value of each team by calculating the mean of xg value of each team\n",
        "    ds = df2.groupby(['teamid'], sort=True, as_index=False)['xg'].mean()\n",
        "\n",
        "    # Storing the winner team of Expected goal battle\n",
        "    Winner = ds.loc[ds['xg'].idxmax()].tolist()[0]\n",
        "\n",
        "    print('Team {} has won the Expected goal battle'.format(Winner))\n",
        "    print('Each team''\\' total expected goal \\n', ds)\n",
        "\n",
        "\n",
        "def part_c():\n",
        "    \"\"\" More info about performance\"\"\"\n",
        "\n",
        "    print('\\n Comparing expected goal value & score of the teams, team {} performed better'.format(Team))\n",
        "\n",
        "\n",
        "part_a()\n",
        "part_b()\n",
        "part_c()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "3ceee930",
      "metadata": {
        "id": "3ceee930"
      },
      "source": [
        "## Q2)\n",
        "### a) Which possessionid had the highest total successful passes? \n",
        "### b) How many successful passes were there and why do you think this specific possession had so many?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c08bdc85",
      "metadata": {
        "scrolled": true,
        "id": "c08bdc85",
        "outputId": "38a357b2-00ac-4c3e-ade9-b74cadc286c8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Possession Id - 417, had the highest total successful passes\n",
            "\n",
            "Total Number of successful passes were 552. \n",
            "There could be many arguments for this, but I believe it will keep the opponent team busy in maintaining thedefensive mode until your team keeps the possession of puck\n"
          ]
        }
      ],
      "source": [
        "# Importing pandas library as pd\n",
        "import pandas as pd\n",
        "\n",
        "# Reading data from csv files\n",
        "df1 = pd.read_csv('Tutorial22_df.csv')\n",
        "df2 = pd.read_csv('Tutorial22_xG_df.csv')\n",
        "\n",
        "\n",
        "def part_a():\n",
        "    \"\"\" Which possessionid had the highest total successful passes? \"\"\"\n",
        "\n",
        "    # Filtering the data frame having successful passes\n",
        "    ds = df1[(df1['eventname'] == 'pass') & (df1['outcome'] == 'successful')]\n",
        "\n",
        "    # Grouping the filtered data by possessionid\n",
        "    ds = ds.groupby(['possessionid'], as_index=False)['eventname'].count()\n",
        "\n",
        "    # Storing the possession id having the max number of successful passes\n",
        "    P_ID = ds.iloc[ds['eventname'].idxmax()].tolist()[0]\n",
        "\n",
        "    print('Possession Id - {}, had the highest total successful passes'.format(P_ID) + '\\n')\n",
        "\n",
        "\n",
        "\n",
        "def part_b():\n",
        "    \"\"\" How many successful passes were there and why do you think this specific possession had so many? \"\"\"\n",
        "\n",
        "    # Fetching the count of dataset having successful passes\n",
        "    ds = df1[(df1['eventname'] == 'pass') & (df1['outcome'] == 'successful')].count()\n",
        "\n",
        "    # Storing the count of such passes\n",
        "    NumOfSuccesPasses = ds['outcome']\n",
        "\n",
        "    print('Total Number of successful passes were {}. '.format(NumOfSuccesPasses))\n",
        "    print('There could be many arguments for this, but I believe it will keep the opponent team busy in maintaining the'\n",
        "          'defensive mode until your team keeps the possession of puck')\n",
        "\n",
        "part_a()\n",
        "part_b()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "bd50c34d",
      "metadata": {
        "id": "bd50c34d"
      },
      "source": [
        "## Q3)\n",
        "### a) Using the event data provided along with x/y coordinate columns, can you identify the likely xCoord of each blueline?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "154e09ed",
      "metadata": {
        "id": "154e09ed",
        "outputId": "79d3d1b4-02f9-43e6-f008-7717a7c1c009"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Likely xCoord of Offensive blue line :  57.32828397442983\n",
            "Likely xCoord of Defensive blue line :  -59.50543193527885\n"
          ]
        }
      ],
      "source": [
        "# Importing pandas library as pd\n",
        "import pandas as pd\n",
        "\n",
        "# Reading data from csv files\n",
        "df1 = pd.read_csv('Tutorial22_df.csv')\n",
        "\n",
        "\n",
        "def part_a():\n",
        "    \"\"\" Using the event data provided along with x/y coordinate columns, can you identify the likely xCoord of each\n",
        "    blueline?\"\"\"\n",
        "\n",
        "    # Filtering the dataset by specific zones & grouping them by possession ID\n",
        "    dZone = df1[df1[\"zone\"] == \"dz\"].groupby(\"possessionid\")\n",
        "    oZone = df1[df1[\"zone\"] == \"oz\"].groupby(\"possessionid\")\n",
        "\n",
        "    # Calculating the mean of x-coordinates of each zones\n",
        "    oZone_xCoord = oZone[\"xcoord\"].mean()\n",
        "    dZone_xCoord = dZone[\"xcoord\"].mean()\n",
        "\n",
        "    print(\"Likely xCoord of Offensive blue line : \", oZone_xCoord.mean())\n",
        "    print(\"Likely xCoord of Defensive blue line : \", dZone_xCoord.mean())\n",
        "\n",
        "\n",
        "part_a()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "15e4e1f4",
      "metadata": {
        "id": "15e4e1f4"
      },
      "source": [
        "## Q4)\n",
        "### a) Create a subset of all shot attempts in the game and then with the plotting library of your choice, produce one scatter plot per team to illustrate where their shots were located and highlight any goals that were scored.\n",
        "### b) Describe in 2-4 sentences your findings for each team."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "639a3519",
      "metadata": {
        "id": "639a3519",
        "outputId": "1d906bd2-4864-4097-f790-62196093bf3e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": "<Figure size 640x480 with 1 Axes>",
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAj4AAAHHCAYAAAC/R1LgAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAB8iklEQVR4nO3dd1xTZ98G8OskYYpMGSKg4kZx4cI9qLhq1brqHnWvVtuqHY6q1VYft3XVXa171W1ddeBCcYsLt+BkyE5yv3/wkhrZGhJCru/zyecp59ycc3GM5sc595CEEAJEREREJkBm6ABERERE+sLCh4iIiEwGCx8iIiIyGSx8iIiIyGSw8CEiIiKTwcKHiIiITAYLHyIiIjIZLHyIiIjIZLDwISIiIpPBwoeIiAAAkiRhwoQJho5BlKtY+BAZmCRJ2XodPXrU0FEztXLlykzzr127VtN269at6NSpE7y9vWFtbY0yZcpg1KhRiIyMzPQcd+/ehaWlJSRJwvnz57OV6/79++jduzdKlCgBS0tLuLm5oX79+hg/fvzH/LiZ2rNnT7oFRFxcHCZMmKDXP8v79+9r/TnI5XJ4eXmhbdu2CAkJ0ck5rl+/jgkTJuD+/fs6OR5RblIYOgCRqVuzZo3W16tXr8bBgwfTbC9Xrpw+Y+VY/fr102QGgFmzZuHSpUto0qSJZlv//v3h7u6Obt26wcvLC1euXMH8+fOxZ88eXLhwAVZWVume4+uvv4ZCoUBiYmK2Mt25cwfVq1eHlZUV+vTpg2LFiuHZs2e4cOECfv31V0ycOPHDftgs7NmzBwsWLEhT/MTFxWnO2bBhw1w5d0a++OILtGjRAiqVCjdu3MDChQuxd+9enD59GpUrV/6oY1+/fh0TJ05Ew4YNUaxYMZ3kJcotLHyIDKxbt25aX58+fRoHDx5Msz2v8/b2hre3t9a2+Ph4DB48GI0bN4abm5tm++bNm9N88Pv5+aFnz55Yu3YtvvzyyzTH379/P/bv34/vvvsOkydPzlamWbNm4e3btwgJCUHRokW19j1//jybP1neFxsbiwIFCmTapmrVqlrvqTp16qB169ZYuHAhFi9enNsRifIMPuoiMgJqtRqzZ89G+fLlYWlpCVdXVwwYMABv3rzRardjxw60bNkS7u7usLCwQIkSJTBp0iSoVCqtdg0bNkSFChVw+fJlNGjQANbW1ihZsiQ2b94MADh27Bhq1qwJKysrlClTBv/8888H5f77778RExODrl27pjn/+9q2bQsAuHHjRpp9ycnJGDFiBEaMGIESJUpk+/x3796Fh4dHmqIHAFxcXNJs27t3Lxo0aICCBQvC1tYW1atXx7p16zT7jx8/jg4dOsDLywsWFhbw9PTE119/jfj4eE2bXr16YcGCBQC0H2Pev38fzs7OAICJEydqtr97V+jmzZto3749HB0dYWlpiWrVqmHnzp1aGVMfKR47dgyDBw+Gi4sLPDw8sn1NUjVu3BgAEBYWlmm7ixcvonnz5rC1tYWNjQ2aNGmC06dPa+Xp0KEDAKBRo0ZG82iWTBfv+BAZgQEDBmDlypXo3bs3hg8fjrCwMMyfPx8XL17EyZMnYWZmBiDlQ8jGxgYjR46EjY0NDh8+jHHjxiE6OhrTp0/XOuabN2/QqlUrdO7cGR06dMDChQvRuXNnrF27Fl999RUGDhyILl26YPr06Wjfvj0ePXqEggUL5ij32rVrYWVlhXbt2mXZNjw8HABQqFChNPtmz56NN2/e4Mcff8TWrVuzff6iRYvin3/+weHDhzUf9BlZuXIl+vTpg/Lly2Ps2LGwt7fHxYsXsW/fPnTp0gUAsGnTJsTFxWHQoEFwcnLC2bNnMW/ePDx+/BibNm0CkPJn9fTp0zSPK52dnbFw4UIMGjQIbdu21VyTihUrAgCuXbuGOnXqoEiRIhgzZgwKFCiAjRs3ok2bNtiyZYumMEw1ePBgODs7Y9y4cYiNjc32NUl19+5dAICTk1OGba5du4Z69erB1tYW3333HczMzLB48WI0bNhQUxzXr18fw4cPx9y5c/H9999rHsnm9UezZMIEEeUpQ4YMEe/+1Tx+/LgAINauXavVbt++fWm2x8XFpTnegAEDhLW1tUhISNBsa9CggQAg1q1bp9l28+ZNAUDIZDJx+vRpzfb9+/cLAGLFihU5+jlevXolzM3NRceOHbPVvm/fvkIul4tbt25pbX/27JkoWLCgWLx4sRBCiBUrVggA4ty5c1ke8+rVq8LKykoAEJUrVxYjRowQ27dvF7GxsVrtIiMjRcGCBUXNmjVFfHy81j61Wq357/Su79SpU4UkSeLBgweabe//GaZ68eKFACDGjx+fZl+TJk2Er6+v1p+TWq0WtWvXFqVKldJsS/3569atK5RKZZbXICwsTAAQEydOFC9evBDh4eHi6NGjokqVKgKA2LJli6bt+9natGkjzM3Nxd27dzXbnj59KgoWLCjq16+v2bZp0yYBQBw5ciTLPESGxkddRHncpk2bYGdnh08++QQvX77UvPz8/GBjY4MjR45o2r7bKTgmJgYvX75EvXr1EBcXh5s3b2od18bGBp07d9Z8XaZMGdjb26NcuXKoWbOmZnvqf9+7dy9HuTdv3oykpKQ0j7nSs27dOixbtgyjRo1CqVKltPaNHj0a3t7e6fb7yUr58uUREhKCbt264f79+5gzZw7atGkDV1dXLF26VNPu4MGDiImJwZgxY2Bpaal1DEmSNP/97vWNjY3Fy5cvUbt2bQghcPHixRznS/X69WscPnwYHTt21Py5vXz5Eq9evUJgYCBu376NJ0+eaH1Pv379IJfLs32O8ePHw9nZGW5ubmjYsCHu3r2LX3/9NcO7cSqVCgcOHECbNm20+m4VLlwYXbp0wYkTJxAdHf1hPzCRAfFRF1Eed/v2bURFRaXbJwXQ7qR77do1/Pjjjzh8+HCaD6WoqCitrz08PLQ+1AHAzs4Onp6eabYBSNOfKCtr166Fo6Mjmjdvnmm748ePo2/fvggMDMSUKVO09p0+fRpr1qzBoUOHIJN92O9ppUuXxpo1a6BSqXD9+nXs2rULv/32G/r374/ixYsjICBA89inQoUKmR7r4cOHGDduHHbu3Jnmerx/fXPizp07EELgp59+wk8//ZRum+fPn6NIkSKar4sXL56jc/Tv3x8dOnSATCaDvb09ypcvDwsLiwzbv3jxAnFxcShTpkyafeXKlYNarcajR49Qvnz5HOUgMjQWPkR5nFqthouLi9Y8OO9K7TAbGRmJBg0awNbWFj///LNm3poLFy5g9OjRUKvVWt+X0d2CjLYLIbKd+eHDhzh+/Dj69++v6X+UnkuXLqF169aoUKECNm/eDIVC+5+k7777DvXq1UPx4sU1c8S8fPkSAPDs2TM8fPgQXl5e2cokl8vh6+sLX19f+Pv7o1GjRli7di0CAgKy9f0qlQqffPIJXr9+jdGjR6Ns2bIoUKAAnjx5gl69eqW5vjmR+r3ffPMNAgMD021TsmRJra8zGvKfkVKlSmX7ZyXKz1j4EOVxJUqUwD///IM6depk+mF39OhRvHr1Clu3bkX9+vU127MatZMb/vrrLwghMn3MdffuXTRr1gwuLi7Ys2cPbGxs0rR5+PAhHjx4kO7djdatW8POzi7LSQ/TU61aNQApxRMAzUixq1evpikwUl25cgW3bt3CqlWr0KNHD832gwcPpmn7/p20rLanPkoyMzPLM8WJs7MzrK2tERoammbfzZs3IZPJNHcHM/q5iPIi9vEhyuM6duwIlUqFSZMmpdmnVCo1H/ypd2revTOTlJSE33//XS8537Vu3Tp4eXmhbt266e4PDw9H06ZNIZPJsH//fs1dq/ctWbIE27Zt03oNGzYMADBjxowM74KlOn78OJKTk9Ns37NnDwBoHuM0bdoUBQsWxNSpU5GQkKDVNvV6pnd9hRCYM2dOmuOnzqnzflFmbW2d7nYXFxc0bNgQixcv1hRj73rx4kWGP2NukcvlaNq0KXbs2KE1I3NERATWrVuHunXrwtbWFkDGPy9RXsQ7PkR5XIMGDTBgwABMnToVISEhaNq0KczMzHD79m1s2rQJc+bMQfv27VG7dm04ODigZ8+eGD58OCRJwpo1a3L0iEoXrl69isuXL2PMmDEZ3glo1qwZ7t27h++++w4nTpzAiRMnNPtcXV3xySefAEgpSN6X+uHaoEEDzZ2bjPz6668IDg5Gu3btNMPGL1y4gNWrV8PR0RFfffUVAMDW1hazZs3Cl19+ierVq6NLly5wcHDApUuXEBcXh1WrVqFs2bIoUaIEvvnmGzx58gS2trbYsmVLun2f/Pz8AADDhw9HYGAg5HI5OnfuDCsrK/j4+GDDhg0oXbo0HB0dUaFCBVSoUAELFixA3bp14evri379+sHb2xsREREICgrC48ePcenSpcwvfC6YPHkyDh48iLp162Lw4MFQKBRYvHgxEhMT8dtvv2naVa5cGXK5HL/++iuioqJgYWGBxo0bZ9gvjcigDDaejIjSldFQ6CVLlgg/Pz9hZWUlChYsKHx9fcV3330nnj59qmlz8uRJUatWLWFlZSXc3d3Fd999pxmO/u5Q4wYNGojy5cunOUfRokVFy5Yt02wHIIYMGZKt/GPGjBEAxOXLlzNsAyDDV4MGDTI9fk6Gs588eVIMGTJEVKhQQdjZ2QkzMzPh5eUlevXqpTVEO9XOnTtF7dq1hZWVlbC1tRU1atQQf/31l2b/9evXRUBAgLCxsRGFChUS/fr1E5cuXUoz3F+pVIphw4YJZ2dnIUmS1p/nqVOnhJ+fnzA3N08zfPzu3buiR48ews3NTZiZmYkiRYqIVq1aic2bN3/Qzy/Ef8PZp0+fnmXb9/MIIcSFCxdEYGCgsLGxEdbW1qJRo0bi1KlTab536dKlwtvbW8jlcg5tpzxNEkLPvw4SERERGQj7+BAREZHJYOFDREREJoOFDxEREZkMFj5ERERkMlj4EBERkclg4UNEREQmgxMYvketVuPp06coWLAgp2EnIiIyEkIIxMTEwN3dPdNFjVn4vOfp06dpVqcmIiIi4/Do0SN4eHhkuJ+Fz3sKFiwIIOXCpa5DQ0RERHlbdHQ0PD09NZ/jGWHh857Ux1u2trYsfIiIiIxMVt1U2LmZiIiITAYLHyIiIjIZLHyIiIjIZLDwISIiIpPBwoeIiIhMBgsfIiIiMhksfIiIiMhksPAhIiIik8HCh4iIiEwGCx/Kkx5HP8aYf8bAc5Yn7KbZofrS6lhxcQWSVcmGjkZEREbMaAufadOmQZIkfPXVV5ptCQkJGDJkCJycnGBjY4PPP/8cERERhgtJHyQkPAS+C30x49QMPI5+jOjEaFx4dgF9dvZBy3UtkahMNHREIiIyUkZZ+Jw7dw6LFy9GxYoVtbZ//fXX+Pvvv7Fp0yYcO3YMT58+Rbt27QyUkj6ESq3CZ+s/Q0xiDFRCpdmuFmoAwKGwQ/jl+C+GikdEREbO6Aqft2/fomvXrli6dCkcHBw026OiorBs2TLMnDkTjRs3hp+fH1asWIFTp07h9OnTBkxMObHn9h48jHqoVfS8Sy3UmH9uPpJUSXpORkRE+YHRFT5DhgxBy5YtERAQoLU9ODgYycnJWtvLli0LLy8vBAUFZXi8xMREREdHa73IcE4/Pg0zmVmmbV7Hv0bYmzA9JSIiovxEYegAObF+/XpcuHAB586dS7MvPDwc5ubmsLe319ru6uqK8PDwDI85depUTJw4UddR6QPJZXIIiCzbKWRG9dYlIqI8wmju+Dx69AgjRozA2rVrYWlpqbPjjh07FlFRUZrXo0ePdHZsyrlPvD+BUq3MtI2XnReKOxTXUyIiIspPjKbwCQ4OxvPnz1G1alUoFAooFAocO3YMc+fOhUKhgKurK5KSkhAZGan1fREREXBzc8vwuBYWFrC1tdV6keHU9aqLqoWrQiFlfEfnu9rfQSYZzVuXiIjyEKP59GjSpAmuXLmCkJAQzatatWro2rWr5r/NzMxw6NAhzfeEhobi4cOH8Pf3N2ByyglJkrCj8w7NHZ3UAif10dbg6oMxuPpgg+UjIiLjZjQdJQoWLIgKFSpobStQoACcnJw02/v27YuRI0fC0dERtra2GDZsGPz9/VGrVi1DRKYP5GHrgUsDL2HjtY346+pfiEyIRLlC5dDPrx9qe9Y2dDwiIjJiRlP4ZMesWbMgk8nw+eefIzExEYGBgfj9998NHYs+gJWZFXpW7omelXsaOgoREeUjkhAi6yE0JiQ6Ohp2dnaIiopifx8iIiIjkd3Pb6Pp40NERET0sVj4EBERkclg4UNEREQmg4UPERERmQwWPkRERGQyWPgQERGRyWDhQ0RERCaDhQ8RERGZDBY+REREZDLy1ZIV9J/7kfex9cZWxCTGoLRTabQt1xaWCktDxyIiIjIoFj75TKIyEQN3D8SqkFWQJAlySY5kdTIcLB2w/LPlaFO2jaEjEhERGQwfdeUzX/79JVZfWg0BAbVQI1mdDACITIjE5xs/x9H7Rw0bkIiIyIBY+OQjt1/dxp+X/4RaqNPsE0hZi3b80fH6jkVERJRnsPDJRzZe2wi5JM9wv1qo8e+DfxHxNkKPqYiIiPIOFj75SGRCJGRS1n+kUYlRekhDRESU97DwyUdKOJaAUq3MtI253BzuBd31lIiIiChvYeGTj3xR4YtMh6wrZAp08e0CG3MbPaYiIiLKO1j45CN2lnaY32I+AECCpLVPISngbO2MyY0mf/R5ohKiMP/sfHyx5Qt03doVf1z4A3HJcR99XCIiotwmCSGEoUPkJdHR0bCzs0NUVBRsbW0NHeeDbL+5HeOOjMOV51cApNzp6Vi+I34N+BUeth4fdewjYUfw2frP8DbpLSRJggQJKqFCIatC2NttL6q5V9PFj0BERJQj2f38ZuHznvxQ+ACAEAL33txDdGI0itoXhaOV40cfM+xNGMr/Xh6JqsQ0Q+blkhwFLQri9rDbKGRd6KPPRURElBPZ/fzmo658SpIklHAsgSqFq+ik6AGA+WfnI0mVlO48QSqhQnRiNP648IdOzkVERJQbWPhQtm29uRUqocpwv1qose3mNj0mIiIiyhmu1UUQQuDo/aNYe2UtXsa9RFG7ouhbtS8qulbUapeoTMzyWPHJ8bkVk4iI6KOx8DFxsUmxaLuhLQ7eOwiFTAGlWgmFTIG5Z+dicPXBmNd8nmZSRL/Cfth7Z2+Gd30UMgU7NxMRUZ7GR10mrt/f/XAo7BAAaCY/TP3/38/9juknp2vaDqkxJNNHXUq1EoOrD87FtERERB+HhY8JexD5AOuvrk+3s3Kq3079hiRVEgAgsEQghtUYBgBaS2Okrg82qdEk3vEhIqI8jYWPCdt/d79m1faMvI5/jfNPzwNIGSk2p9kcrG23FlULV03ZBgn+nv7Y0XkHfqz/Y65nJiIi+hjs42PCEpWJkCBlWfy826lZkiR08e2CLr5dNI/EFDK+jYiIyDjwE8uEVSlcJcuiRyFToLxL+Qz3ERERGRM+6jJhdTzrwMfZR9NH530KSYEOPh3gUsBFz8mIiIhyBwsfEyZJEtZ/vh62FrZp7t7IJTmKOxTHnGZzDJSOiIhI94ym8Fm4cCEqVqwIW1tb2Nrawt/fH3v37tXsT0hIwJAhQ+Dk5AQbGxt8/vnniIiIMGBi4+Dr6ouLAy5iULVBsLVIWdvEzcYNP9b/EWf7nYVzAWcDJyQiItIdo1mk9O+//4ZcLkepUqUghMCqVaswffp0XLx4EeXLl8egQYOwe/durFy5EnZ2dhg6dChkMhlOnjyZo/Pkl0VKP5RaqLWGqhMRERkDk1id3dHREdOnT0f79u3h7OyMdevWoX379gCAmzdvoly5cggKCkKtWrWyfUxTL3yIiIiMUXY/v41yWI5KpcKmTZsQGxsLf39/BAcHIzk5GQEBAZo2ZcuWhZeXV5aFT2JiIhIT/xuuHR0dnavZiUzRzZc3sej8Ipx9chYWcgt8WuZT9KrcC45WjoaORkQmxqgKnytXrsDf3x8JCQmwsbHBtm3b4OPjg5CQEJibm8Pe3l6rvaurK8LDwzM95tSpUzFx4sRcTE1k2uafnY/he4dDLsmhFClzPx17cAyT/52Mg90Pws/dz8AJiciUGFVnjjJlyiAkJARnzpzBoEGD0LNnT1y/fv2jjjl27FhERUVpXo8ePdJRWiI6EnYEw/YOg4DQFD0AICAQnRiNwD8D8TbprQETEpGpMarCx9zcHCVLloSfnx+mTp2KSpUqYc6cOXBzc0NSUhIiIyO12kdERMDNzS3TY1pYWGhGiqW+iEg3ZpyakeE8USqhwuv411h7ea2eUxGRKTOqwud9arUaiYmJ8PPzg5mZGQ4dOqTZFxoaiocPH8Lf39+ACYlMlxACB+8dhEqoMm138N5BPSUiIjKiPj5jx45F8+bN4eXlhZiYGKxbtw5Hjx7F/v37YWdnh759+2LkyJFwdHSEra0thg0bBn9//xyN6CIi3cqq6BEQmjXfiPKD+OR4bLy2EcHPgmEuN0eLUi3QqFgjSJJk6Gj0/4ym8Hn+/Dl69OiBZ8+ewc7ODhUrVsT+/fvxySefAABmzZoFmUyGzz//HImJiQgMDMTvv/9u4NREpkuSJNQoUgNnn5yFWqjTbSOTZKjlwV9OKH84dO8Q2m9qj8iESJjJzCAg8L+g/6GKWxXs6rIL7gXdDR2RYOTz+OQGzuNDpDsbrm5A5y2d090nQYK53BwPv37I9eDI6F17fg1+S/yQrE5OU+grZAqUciyFSwMvwUxuZqCE+V92P7+Nuo8PEeVtHct3xNAaQwFAq5OzQqaAXCbHxg4bWfRQvjDj1AyohCrdu5tKtRI3Xt7AjtAdBkhG72PhQ0S5RpIkzG02Fzs670Cj4o1gb2kPlwIu6F25Ny4OuIjWZVobOiKRTmy6vinT/mpySY4tN7boMRFlxGj6+BCRcZIkCa3LtGaRQ/mWEALxyvhM26iECm8TOWdVXsA7PkRERB9BkiSUciwFCRmP3JJLcpRzLqfHVJQRFj5EREQfaUj1IZnuVws1+lXtp6c0lBkWPkRERB9pQLUBaFisIWSS9sdq6tdTm0xFKadShohG72HhQ0RE9JHM5ebY23UvJjSYAGdrZ832iq4VsbH9RoyuO9qA6ehdnMfnPZzHh4iIPoZSrUT423CYy805XYMeZffzm6O6iIiIdEghU8DD1sPQMSgDfNRFREREJoN3fIiIKI1L4Zfwx4U/cPv1bThYOaBT+U5oVboVFDJ+bJBx4zuYiIg0hBD49uC3+F/Q/6CQKaBUKyGX5Fh/dT38Cvthf7f9cLJ2MnRMog/GR11ERKSx8PxC/C/ofwCgWYJBJVQAgJDwEHTc1NFg2Yh0gYUPEREBAFRqFaadmJbxfqHC4fuHERIeor9QRDrGwoeIiAAAt17dwqPoR5m2kUty7L29V0+JiHSPhQ8REQEAklRJWbaRJClb7YjyKhY+REQEACjlVAoFzApk2kapVqKaezU9JSLSPRY+lKfFJsUi4m2EppMlEeUeazNr9KvaD3JJnu5+uSSHl50XmpVspudkRLrDwofypLNPzuLTvz6F7TRbuP3PDU6/OWHU/lF4Hf/a0NGI8rVJjSehauGqkP7/f6kUMgWszayxteNWyGXpF0ZExoBrdb2Ha3UZ3t7be9F6fWsIITTDaIGU3zaLOxRHUN8gFLIuZMCERPlbfHI8Fp5fiIXnFuJ+1H0UNC+Irr5d8bX/1/B28DZ0PKJ0Zffzm4XPe1j4GFaiMhHu/3PHm4Q3EEj71pRLcvSt0heLP11sgHRERJRXZffzm4+6KE/ZdnMbXie8TrfoAVLmEVl9eTViEmP0nIyIiPIDFj6Up1x9fhVmMrNM2yQoE/Ag6oGeEhERUX7CwofylAJmBaAW6izbWZtZ6yENERHlNyx8KE9pU7aNVofm90mQUN65PIrbF9djKiIiyi9Y+FCeUs65HNqWbZvhPCICAuMbjIckSenuJyIiygwLH8pzVrddjcASgQBS5g5RyBSQSTIoZArMbTYXHcp3MHBCIiIyVgpDByB6n425DXZ33Y1zT85h47WNiEqMQknHkuhZqSdcbVwNHY+IiIwYCx/Ks6oXqY7qRaobOgYREeUjfNRFREREJoOFDxEREZkMFj5ERERkMoym8Jk6dSqqV6+OggULwsXFBW3atEFoaKhWm4SEBAwZMgROTk6wsbHB559/joiICAMlJiIiorzGaAqfY8eOYciQITh9+jQOHjyI5ORkNG3aFLGxsZo2X3/9Nf7++29s2rQJx44dw9OnT9GuXTsDpiYiIqK8xGhXZ3/x4gVcXFxw7Ngx1K9fH1FRUXB2dsa6devQvn17AMDNmzdRrlw5BAUFoVatWtk6LldnJyIiMj75fnX2qKgoAICjoyMAIDg4GMnJyQgICNC0KVu2LLy8vBAUFJThcRITExEdHa31ovwhWZWM2KRYGGltT0REucAo5/FRq9X46quvUKdOHVSoUAEAEB4eDnNzc9jb22u1dXV1RXh4eIbHmjp1KiZOnJibcUnPTj48iWknp2HP7T1QCzU8bT0xtMZQjKg5AhYKC0PHI8rUi9gXWBmyEjde3oCNuQ0+L/c56hetz2VaiHTEKAufIUOG4OrVqzhx4sRHH2vs2LEYOXKk5uvo6Gh4enp+9HHJMDZc3YAuW7tAgqRZ5f1R9COMPTQWe27vwb5u+2CpsDRwSqL0/XHhDwzePRgqoYJMSrkhP+/sPNTxrIOdX+yEo5WjgRMSGT+je9Q1dOhQ7Nq1C0eOHIGHh4dmu5ubG5KSkhAZGanVPiIiAm5ubhkez8LCAra2tlovMk6v41+j145eEEKkWeFdLdQ4/vA4ZgXNMlA6osztvb0X/f7uh2R1MtRCDaVaCaVaCQA4/fg02q5vy8e2RDpgNIWPEAJDhw7Ftm3bcPjwYRQvXlxrv5+fH8zMzHDo0CHNttDQUDx8+BD+/v76jksGsPrSaiQqEyGQ/oeDWqgx/9x8fnhQnjT538mauzzvUwkV/n34L848OaPnVET5j9E86hoyZAjWrVuHHTt2oGDBgpp+O3Z2drCysoKdnR369u2LkSNHwtHREba2thg2bBj8/f2zPaKLjNuliEuQS3IohTLDNk9jniIqMQr2lvb6C0aUhVdxr3Dq8alM2yhkCmy/uR21PPjvGdHHMJrCZ+HChQCAhg0bam1fsWIFevXqBQCYNWsWZDIZPv/8cyQmJiIwMBC///67npOSoVgprAAJyOCGj4aFnB2cKW+JS47Lso0EKVvtiChzRlP4ZOfxhKWlJRYsWIAFCxboIRHlNZ+V+QwLzy/McL9ckqNRsUawMrPSYyqirLnZuMHe0h6RCZEZtlGqlajgUkF/oYjyKaPp40OUlU9KfIJKrpWgkKVfz6uFGmPrjdVzKqKsmcnNMMBvAOSSPN39EiRYmVnhiwpf5F6IiAhg1Spg0SIgKAhgXzjKp4zmjg9RVmSSDHu77kXgn4G48vwKFDIFhBAQEJBLciz5dAkaF29s6JiUh4S+DMX+u/uRrEpG9SLVUc+rnsHmy/mh3g/Yf3c/rkRc0RqVmFoMrW6zGgUtCur+xImJwPDhwPLlgPKd/nEVKgDr1gG+vro/J5EBGe2SFbmFS1YY3v3I+9hyfQuiEqNQyrEU2vu0z9HjKZVahf1392PbjW2IV8ajgksF9KnSBy4FXHIxNRmTyIRIdNvaDbtv74ZMkkGCBJVQoVyhctjccTN8nH0Mkutt0lv8dvI3LDy/EC/jXkKChOYlm+P7et+jjlcd3Z9QCKBDB2DbNkCt1t4nlwM2NsCFC4C3t+7PTaRj2f38ZuHzHhY+hpOkSsKQ3UOw7OIySJIEuSRHsjoZtha2+OPTP9ChfAdDR6R84EXsC9RZXgd3X9+FGtof9nJJDjtLO1weeBlFbIsYKGHKY9nIhEhYKaxyt0/a2bNAzZoZ71cogL59Ux5/EeVx+X6tLsp/Bu8ejOUhyyEgoBZqJKuTAQAxiTHotLkTDt49aOCEZMwSlYkYumco3Ge64/br22mKHiBlvpyohCjMOTPHAAn/I5NkcLRyzP2O+H/+mVLcZESpBFavTns3iMiIsfChPCHsTRiWX1yuWWbiXQICkiRh3JFxBkhG+YEQAu03tsfC8ws1syFnRCVUWH1ptZ6SGdiLF1kXNfHxKS+ifIKFD+UJm65vynDWWiDl1v/pJ6fxOPqxHlNRfnEo7BB23d6VbmGdnjcJb3I5UR7h6QnIsvgYsLMDrK31k4dID1j4UJ4QmRCZaeGTKiohSg9pKL9ZGbIyw6Hi6fGy88rFNHlI797aI7neJ5cD/foBXBme8hEWPpQnlHQsmeUjCIVMAQ9bj0zbEKXnUfSjNAvXZkSChIF+A3M5UR5RrhwwbFj6+xQKoHBh4Ntv9ZuJKJex8KE8oWP5jrA2y/h2ukJSoFP5TrCztNNjKsovihQskq07PnJJjkpulTCwmokUPgAwezYwdSrg4PDfNkkCWrQATp8GXDgNBOUvLHwoT7Axt8GiVosgQUrzyEshU6BQgUKY2mSqgdKRsetZqWeWd3wUkgJ9qvTB0Z5HUcC8gJ6S5QEyGTBmDPDsGXD0KLBvH/DwIbBjB1DEcEP6iXILZ26mPKNbxW5wsHTAT0d+wsXwiwBSip4OPh3wa8Cv8LTzNHBCMlaflPgEgSUCcfDewTQdnOWSHM4FnBHUJwjFHIoZJmBeYGEBNGhg6BREuY4TGL6HExjmDWFvwhCdGA0vOy84WDlk/Q1EWYhPjseIfSOwImSFVn+yT7w/wYrPVhh0wkIi+nicufkDsfAhyt9exL7A0ftHoVQrUc29Gko5lTJ0JCLSgex+fvNRF1EmohOjsfbyWpx7eg7mcnO0KNUCLUu1hFyW/aHRlLc4F3DO9eVP1EKNfXf2YcfNHYhXxqOia0X0qtwLhawL5ep5iShrvOPzHt7xoVR7bu9Bx00dEZccpyl0lGolSjmWwv5u+1HcobiBE1Je9CzmGZqtbYbLEZehkCkghICAgEKmwLLWy9CtYjdDRyTKl7hWF9FHuBJxBW3Wt0FcchwEBJRqpaZfSNibMDRZ3QSJykQDp6S8Ri3UaLa2Ga6/uA4gpVBWCRXUQo0kVRJ6bOuBY/ePGTglkWlj4UOUjplBMyH+/3/vUwolwiLDsPn6ZgMko7xs3519uBxxOcPJOGWSDNNOTNNzKiJ6FwsfonRsvrE505mkZZIM20O36y8QGYUdN3dAIcu466RKqLD/7n7eLSQyIBY+ROlIUCZkul8t1IhNitVTGjIW8cp4ZNVtUkAgSZWkp0RE9D4WPkTp8HH2gYSMF2aUS3L4uvjqMREZg4quFdN9PPouD1sP2Jjb6CkREb2PhQ9ROobVGJbpB5haqNHPr58eE5Ex6FW5V6aPumSSDEOrD4XE1c6JDIaFD1E6elXuhU9Lf5rmrk/qQpczA2eipGNJQ0SjPKyQdSEsa70MEqQ0i6LKJBnqedXDV7W+Mkw4IgLAwocoXQqZAls7bcXMwJkoZldMs93fwx9/f/E3P7woQ90qdsORnkfwifcnmsK5SMEimNJ4CvZ32w8LhYWBExKZNk5g+B5OYEjvE0IgKjEKZjIz01q1mz5aojIRSaok2Jjb8PEWUS7jkhVEOiJJEuwt7Q0dg4yQhcLCpO/wCCEQ9DgIKy6uwOOYx3CzcUP3it3RqFgjSJKEx9GPMffMXKy5vAZRCVHwdvDGoGqD0LdqX1gqLA0dn/Ip3vF5D+/4EBF9PKVaiZ7bemLd1XVQyBRQqpWa/29Wohl+bvQzAv8MRHRiNFRCBQCaR4O1PGrhYPeDvMNKOcIlK4iIyGB+OvwT/rr6FwBoJgNN/f8D9w6gyeomWkUPAM1s6WefnMWPh3/Uf2gyCSx8iIhIp94mvcXcs3MznBJCLdSISYrRKnrepRIqLL2wlJOEUq5g4UNERDp18uFJxCXHfdQxYpNjcevVLR0lIvoPCx8iItIpXS3JkdlkkEQfyqgKn3///Reffvop3N3dIUkStm/frrVfCIFx48ahcOHCsLKyQkBAAG7fvm2YsEREJqpK4SqZLvmSHYVtCqOcczkdJUrrZdxLLDi7AD8e/hHzz87Hi9gXuXYuyluMqvCJjY1FpUqVsGDBgnT3//bbb5g7dy4WLVqEM2fOoECBAggMDERCQuYLThIRke542HqgdZnWGd6xUcgUsLWwTTO79bu+qf1NrtzxEUJg6vGpcP+fO4btHYbfTv6GEftGwH2mOyYdm5TlIrNk/Iyq8GnevDkmT56Mtm3bptknhMDs2bPx448/4rPPPkPFihWxevVqPH36NM2dISIiyl2LWi2Cp60nZJL2x4xcksPJygn/dP8H5V3KA4CmTWqhM8BvQK7Njj73zFx8f/h7JKuTISCQrE6GWqihVCsx7ug4zDo9K1fOS3mHURU+mQkLC0N4eDgCAgI02+zs7FCzZk0EBQUZMBkRkelxs3FDcP9gjG8wHkUKFoFMksGlgAu+rf0tQgaGoHqR6jjf7zw2tt+I1qVbo37R+uhZqSeC+gZhUatFaQomXUhUJmLisYmZtvn52M+IT47X+bkp78g3PcfCw8MBAK6urlrbXV1dNfvSk5iYiMTERM3X0dHRuROQiMjEOFg5YFyDcRjXYFy6+83kZuhQvgM6lO+glzxH7h/Bm4Q3mbaJSozC4bDDaFm6pV4ykf7lmzs+H2rq1Kmws7PTvDw9PQ0diYiIckFUQlT22iVmrx0Zp3xT+Li5uQEAIiIitLZHRERo9qVn7NixiIqK0rwePXqUqzmJiMgwSjmVyla7ko4lczkJGVK+KXyKFy8ONzc3HDp0SLMtOjoaZ86cgb+/f4bfZ2FhAVtbW60XERHlP1XcqqCSa6UM+w/JJBl8nH1Q3b26npORPmWrj8/OnTuzfcDWrVt/cJisvH37Fnfu3NF8HRYWhpCQEDg6OsLLywtfffUVJk+ejFKlSqF48eL46aef4O7ujjZt2uRaJiIiMg6SJGHpp0vRYGUDJKmStJbMkEtymMnNsKz1MkjSx81BRGmdfXIWc8/MxZH7RyBBwifen2BYzWGoWriq3rNka3V2mSx7N4YkSYJKlf7aK7pw9OhRNGrUKM32nj17YuXKlRBCYPz48ViyZAkiIyNRt25d/P777yhdunS2z8HV2YmI8reQ8BB8f+h77LuzDwICEiQElgjElCZTDPJBnN/9fu53DNkzBAqZQrNQrUKmgEqtwh+t/0CfKn10cp7sfn5nq/AxJSx8iIjyH5VahZUhKzHv7DxcfX4V5nJzBJYIRKfyndCoeCO42rhmfRDKseCnwai+tHqGC9ZKkHBl0BXNnE4fI7uf3x/Vx4czIhMRkSHceHEDw/YMQ5XFVVB9aXWMPzIeT2OepttWpVah0+ZO+PLvL3El4gpUQoV4ZTx23d6Fbtu64eSjk3pObzrmn50PuSzjGbrlMjl+P/e7HhN9QOGjUqkwadIkFClSBDY2Nrh37x4A4KeffsKyZct0HpCIiOhdS4OXovzv5bEoeBFCwkNw/ul5TD4+GSXnlsShe4fStr+wFFtvbAUAqKHWbFeqlVALNbps6YJXca/0lj89SrUS229ux+DdgzHg7wFYcXHFR69wnxccvX9U83grPUq1EkfuH9Fjog8ofKZMmYKVK1fit99+g7m5uWZ7hQoV8Mcff+g0HBER0btOPz6NAbsGQEBofaCqhRqJqkS0Xt8az2Ofa33P7NOzMzxe6rIVK0JW5FbkLN1+dRtl5pdB2w1tsfTCUiwPWY4+O/vAY6YHjt0/ZrBcupCdGbhzY5buTM+X029YvXo1lixZgq5du0Iu/+/2VaVKlXDz5k2dhiMiInrX7NOzM3x0ohZqJCgT8MeF/34JT1QmIvRVaIZ9TFIFPwvWac7sepv0Fo1WNcKDyAcAUu6ApBZ0UYlRaL62Oe68vpPZIfK0ZiWbZbrYrFySo1nJZnpM9AGFz5MnT1CyZNrJndRqNZKTk3USioiIKD0H7x7M9NGJWqhx8O5BzddymRwSMh+eLkGCudw80za5Ze3ltXga81RraH0qtVAjWZ2MeWfmGSCZbgypMSTDFe8lSJBJMgyqNkivmXJc+Pj4+OD48eNptm/evBlVqlTRSSgiIqL0vNtHJyPvFhEKmQKfeH8CuZRxB1uVUKFlKcOszbXlxpZM9yvVSmy4tkFPaXTPx9kHf7b7EwqZQuvPQC7JoZApsLHDRpRwLKHXTDlepHTcuHHo2bMnnjx5ArVaja1btyI0NBSrV6/Grl27ciMjERERAKCuV13svb033TskQMoHav2i9bW2ja47GgfuHciwvaedJ9qUbaPrqNnyNultlo/h4pXGvVp85wqdUc29GhadX4RDYYcggwwB3gEYWG0gijsU13ueD5rH5/jx4/j5559x6dIlvH37FlWrVsW4cePQtGnT3MioV5zHh4go7zp07xAC1gSku0+CBIVMgTvD78DLzktr35LgJRi0exAkSFAJFWSSDGqhhpedFw71OGSw9bkG7x6MpReWZvj4TibJ4O/hjxN9Tug5mfHhBIYfiIUPEVHeNuXfKfjxyI9pZgIGgL8+/wvtfdqn+30Pox5iafBSXAy/CCszK7Qu3RodyneApcJSb9nfdyn8Eiovrpxpm3Xt1uEL3y/0E8iI5Xrhc/78edy4cQNASr8fPz+/D0uax7DwISLK+/598C/mnZmHE49OQCFToEXJFhhec7hOZgDWt4lHJ2LCsQmau1AANB2y2/u0x/r26/U+5NsY5Vrh8/jxY3zxxRc4efIk7O3tAQCRkZGoXbs21q9fDw8Pj48KbmgsfHJfkioJj6Mfw0JuAfeC7lwQkIhM3sZrG/HryV9x4dkFAEBx++L4qtZXGFJ9SKYzH9N/cq3wadasGSIjI7Fq1SqUKVMGABAaGorevXvD1tYW+/bt+7jkBsbCJ/fEJsXi52M/Y3HwYkQlRgEAKrhUwI/1fkSnCp0MnI6MjRACT2KeID45Hp52ngZ9XEGkK1EJUVCqlXC0cuQvhTmUa4WPlZUVTp06lWboenBwMOrVq4e4OOOeYpuFT+6IS45D41WNcf7pea3RGBIkCAj8GvArvqvznQETkjHZfH0zJv07CZcjLgMACpoXxJdVv8SEhhNga8G/t0SmKNcWKfX09Ex3okKVSgV3d/ecHo5MxLwz83Du6bk0Q1BTh3GO+WcMwt6EGSIaGZk5p+egw6YOuBJxRbMtJikGc8/MRf0V9RGTGGPAdESU1+W48Jk+fTqGDRuG8+fPa7adP38eI0aMwIwZM3QajvKP38/9rum0lx6ZJNOaZp4oPY+jH2PkgZEAkGbuE5VQ4erzq/hf0P8MEY2IjES2JjB0cHDQetYYGxuLmjVrQqFI+XalUgmFQoE+ffqgTZs2uRKUjFeyKhkPox9m2kYt1Ah9FaqnRGSsVlxckenyAyqhwu/nfsf4BuPZP4KI0pWtwmf27Nm5HIPyM4VMAXO5OZJUSRm2kcvkKGhRUI+pyBjden0ryzYv4l7gbdJbvp+IKF3ZKnx69uyZ2zkoH5MkCR18OmDDtQ0Zzk6qVCvR0aejnpORsSloXjDlTk4mQzLkkpwjvIgoQx81I1JCQgKio6O1XkTpGV1nNOSSPN1JuBSSAlULV0VgyUADJCNj0sGnQ6YrcytkCrQt2xZmcjM9piIiY5Ljwic2NhZDhw6Fi4sLChQoAAcHB60XUXp8XX2xu8tu2FvYAwDMZGaaKeZredTC/m77OTMpZalhsYao61k33ZW2ZZBBgoSx9cYaIJlpC3sThl+O/4Kv932NWUGz8Dz2uaEjEWUox/P4DBkyBEeOHMGkSZPQvXt3LFiwAE+ePMHixYsxbdo0dO3aNbey6gXn8cldCcoEbLm+BRfDL8JSYYlPS3+KGkVqsCMqZdub+DfosKkDDoUdgkKmgAQJyepkOFg6YN3n69CsZDNDRzQZKrUKw/cNx8JzCyGTZJBJMs0CoJMbTcbouqMNHZFMSK5NYOjl5YXVq1ejYcOGsLW1xYULF1CyZEmsWbMGf/31F/bs2fPR4Q2JhQ+RcQh+GoydoTsRr4xHRdeKaO/Tnn179OzbA9/if0H/SzO1QKolrZagn18/PaciU5VrhY+NjQ2uX78OLy8veHh4YOvWrahRowbCwsLg6+uLt2/ffnR4Q2LhQ0SUtVdxr+A+0z3T0ZqFbQrj0dePuNYU6UWuzdzs7e2NsLCUGXbLli2LjRs3AgD+/vtvzaKlRESUv+25vSfTogcAnr19hrNPzuopUUpfo0P3DuHCswvI4e/0ZEKyNZz9Xb1798alS5fQoEEDjBkzBp9++inmz5+P5ORkzJw5MzcyEhFRHhOTFKNZay+rdrntSsQVDN83HEfvH9Vs83bwxtQmU9GxPKfJIG05Lny+/vprzX8HBATg5s2bCA4ORsmSJVGxYkWdhiMiorypjFOZLIseACjtVDpXc1x/cR21l9dGfHK81vZ7b+6h0+ZOeJv0Fn2q9MnVDGRcclz4vK9o0aIoWrSoLrIQEZGRaFS8EYrZF8PDqIfprsMnl+RoXLwxitkXy9Uc3xz4BvHJ8WkWQE41Yt8IdCrfCQXMC+RqDjIe2Sp85s6dm+0DDh8+/IPDUP4ihOAwdaJ8SibJsKrNKjRd0xRKtVKr8FBICtha2GJ+i/m5muFZzDPsu7Mv0ztPb5PeYsuNLehRqUeuZiHjka3CZ9asWdk6mCRJLHxM3OPox5gZNBMrQ1biTcIbFLYpjP5+/TGi5gg4WHGCSyJDSFYl448Lf2DBuQUIfRUKK4UV2vu0xze1v4GPs88HH7d+0fo42eckxh8djz2390BAQCFToFP5Tvi50c/wdvDWan/z5U3MODUDm65vQlxyHEo5lsLg6oPR368/zOXmOT7/4+jHWT5uU8gUeBD5IMfHpvwrx8PZ8zsOZ/9wN1/eRN3ldRGZEKn1259ckqOYfTGc7HMSrjauBkxIZHqSVElota4V/rn3DwBoCgWFTAG5JMfuLrvRxLvJR5/nTfwbvI5/DZcCLukuEHvs/jE0W9sMSrVSs+yIhJQ7wg2LNcTernthobDI0TnD3oTBe653pm0kSFjQYgEGVR+Uo2OT8cm14exE6RFC4IstX6QpegBAJVR4EPkAw/fybiCRvs04NQOHwg5B/P//UinVSiSrk9F+U3vEJcd99HkcrBxQwrFEukVPgjIBn2/8HEmqJK211lIzHXtwDNNOTMvxOYs7FEd19+qZLncjl8nR3qd9jo9N+RcLH9KJc0/PISQ8JMMOhkqhxJYbWxD+NlzPyYhMl0qtwryz89LtfAwAaqFGZEIkNlzdkKs5tlzfglfxrzLNMf/c/EwXoM3ItICUgin17tH7vqv9HZwLOOf4uJR/5cvCZ8GCBShWrBgsLS1Rs2ZNnD2rvwm0TNWFZxcy/IcnlUqocDnisp4SEeUPD6Me4sfDP6L52uZos74N/rjwB2KTYrP1vc9jn2f5y4aZzAznn57XRdQMnX96HmYys0zbvIx7iSfRT3J87MbFG2N7p+1wKeACAJq7PxZyC4yrPw6TGk/KeWDK1z56OHtes2HDBowcORKLFi1CzZo1MXv2bAQGBiI0NBQuLi6GjpdvmcvNszWnh4U8Z8/wiUzZ8ovL0f/v/gCgWfxzR+gO/HTkJxzqcSjLjsnZ6TAsID6oY3FOZPffhw/N8WmZT/G41GPsu7MP997cg72lPVqXaQ17S/sPOh7lb/nujs/MmTPRr18/9O7dGz4+Pli0aBGsra2xfPlyQ0fL15qWaJrpc3YAsLOwQ02PmnpKRGTcjj84ji93fgmVUGkeIac+KnoR+wIBqwPSTNr3PidrJ1Rxq5Lp302lWokWpVroLng6mpdqnuljLBlkqOBSAW42bh98DoVMgValW2F4zeHoUakHix7KUI4Ln3379uHEiROarxcsWIDKlSujS5cuePPmjU7D5VRSUhKCg4MREBCg2SaTyRAQEICgoKB0vycxMRHR0dFaL8o5D1sPdPXtCrmU/mKEEiSM9B/J1bOJsmn6qekZ/n1SCRWevX2Gjdc2Znmc7+t9n2HfGoVMAV8XX52M6spMg6INUMWtChRS+g8Z1FDj+7rfc94v0oscFz7ffvutpji4cuUKRo0ahRYtWiAsLAwjR47UecCcePnyJVQqFVxdtYdMu7q6Ijw8/efcU6dOhZ2dnebl6empj6j50qJWi9CkeMo/oAqZQuv/+1Tpgx/q/WCwbETGRAiBfXf2QSkyuUsiybDnzp4sj9Xepz2mNUnpAJxaSKXeAfJ28MaernuyvFv7sSRJwq4uu1DKqZTW+VMLoZ8b/owvfL/I1QxEqXLcxycsLAw+PinPlbds2YJWrVrhl19+wYULF9CiRe7eLs0NY8eO1SrYoqOjWfx8IGsza+zrtg/HHhzDmktr8DzuObxsvdCnSh/4ufsZOh6R0RAQWY5wEkJkuTp6qtF1R6NtubZYErwE115cQ0HzgmhXrh3alWuX6/17UrkXdEfIwBBsv7kdm69vRkxSDMoVKod+VfuhnHM5vWQgAj6g8DE3N0dcXMqcD//88w969EiZBtzR0dHgj4kKFSoEuVyOiIgIre0RERFwc0v/2bGFhQUsLNjhVlckSULDYg3RsFhDQ0chMloySYbKbpVxKeJSho+pJElCdffq2T5maafSmNF0hq4ifhBzuTk6lu/IFdPJoHJ8f7Nu3boYOXIkJk2ahLNnz6Jly5YAgFu3bsHDw0PnAXPC3Nwcfn5+OHTokGabWq3GoUOH4O/vb8BkREQ5M6LmiAyLHiClQzBXHSfKuRwXPvPnz4dCocDmzZuxcOFCFClSBACwd+9eNGvWTOcBc2rkyJFYunQpVq1ahRs3bmDQoEGIjY1F7969DR2NyOREvI3A1edX8SL2haGjGJ0WpVqggFnGK4rX8arzUaOgiExVjh91eXl5YdeuXWm2Z3ch09zWqVMnvHjxAuPGjUN4eDgqV66Mffv2penwTES5J/hpML4/9D0O3DsAIGVUX8vSLTG1yVRUcKlg4HTGYe6ZuUhQJmS4/9iDYzj/9DyquVfTYyoi45etRUqjo6M1C35l1Y/H2Bf25CKlRB/n1KNTaLyqMZRqZZrFai0UFjjR+wSqFK5iwITGwXWGK57HPs9wv0KmQP+q/bGg5QI9piLKu7L7+Z2tOz4ODg549uwZXFxcYG9vn+5cC0IISJIElSr9tZqIKP8TQqDPjj5IVien6Z+iEiokKhMxYNcAnO3HZWQyoxbqTIseIGXiwccxj/WUiCj/yFbhc/jwYTg6Omr+m5NMEVF6gh4HIfRVaIb7VUKFc0/P4UrEFfi6+uoxmXGRSTLYW9ojMiEywzYKmQIu1lyGhyinslX4NGjQQPPfDRs2zK0sRGTkbr+6nb12r2+z8MlC78q9MffMXK3Hhe9SqpXoUamHnlMRGb8cj+qaMGEC1Oq0QyyjoqLwxReceZPIlNlZ2mWvnUX22pmyUf6j4GDlkO6yFTJJhpalWqKuV10DJCMybjkufJYtW4a6devi3r17mm1Hjx6Fr68v7t69q9NwRGRcPvH+BDbmNpm2KWRdCPWK1tNTorzv4rOLGLx7MAJWB6Djpo7YemMrlGolitgWwck+J9N0BFfIFOhduTc2ddjEbgdEHyDHw9kvX76MAQMGoHLlyvjf//6HW7duYc6cOfj2228xceLE3MhIREaigHkB/FDvB4w9NDbDNuMbjNfbMgl5mRACow6MwqzTs6CQKaBUKyGX5Nh0fROquFXBge4HUNqpNM71O4cLzy7gwrMLsJBb4JMSn3D+HqKPkK3h7On5/vvvMW3aNCgUCuzduxdNmuTu6r76wuHsRB9HCIHxR8dj6ompUAs15JIcSrUSCpkCPzf6GaPrjOadCgDzz87HsL3D0t0nl+SoX7Q+Dvc8rOdURMYru5/fH1T4zJs3D2PGjEGbNm0QHBwMuVyOdevWoVKlSh8VOi9g4UOkGxFvI7Dh2gaEvw1HkYJF0LlCZzhZOxk6Vp6gUqtQbE4xPI7OfDj6hf4XOOcRUTbpdB6fdzVr1gznz5/HqlWr0L59e8THx2PkyJGoVasWJk6ciO++++6jghNR/uBq44rhNYcbOkaedOvVrSyLHrkkx747+1j4EOlYjjs3q1QqXL58Ge3btwcAWFlZYeHChdi8eXOeWbaCiCgvS1IlZdlGkqRstSOinMnxHZ+DBw+mu71ly5a4cuXKRwciIsrvSjmVgo25Dd4mvc2wjVKtRPUi1fWYyjCEELgYfhG3Xt2CnYUdGhVvBEuFpaFjUT6W48InM4UKFdLl4YiI8iVrM2t8WeVLzDs7L90JCuWSHB62HggsEWiAdPpz/ul5fLnzS1yKuKTZZmdhh3ENxuHrWl+zEzzlig961DVjxgzUqFEDbm5ucHR01HoREVHWJjWehGru1SD9//9SySU5bMxtsLXTVshlaScvzC8uR1xG/RX1cfX5Va3tUYlRGHVgFCb9O8lAySi/y3HhM3HiRMycOROdOnVCVFQURo4ciXbt2kEmk2HChAm5EJGIKP+xMbfBkZ5HMCtwFko7lYa53ByFrAthaI2hCBkYgqqFqxo6Yq764fAPSFIlZbgkx6R/J2W5UCvRh8jxcPYSJUpg7ty5aNmyJQoWLIiQkBDNttOnT2PdunW5lVUvOJydiCh3vYx7CZfpLhDI+ONHJskws+lMjKg1Qo/JyJhl9/M7x3d8wsPD4eubsrigjY0NoqKiAACtWrXC7t27PzAuERGZiuexzzMteoCUR37P3j7TUyIyJTkufDw8PPDsWcqbsUSJEjhw4AAA4Ny5c7CwsNBtOiIiyndcCrho9WtKj0qoUNimsJ4SkSnJceHTtm1bHDp0CAAwbNgw/PTTTyhVqhR69OiBPn366DwgERHlL4WsC6FFqRbprjyfSibJ8IXvF3pMRabig9fqShUUFISgoCCUKlUKn376qa5yGQz7+BAR5b7LEZdR649aGXZwntBgAsY3HG+AZGSscnWtrvyMhQ8RkX6ce3IOfXf2xZXn/01+a2dhh5/q/4SR/iM5jw/lSK6t1fUuW1tbhISEwNvb+2MOQ0REJqh6keq4NPASgp8F4/ar27C1sEXj4o1hZWZl6GiUj2W78Hn69Cnc3d21tvFmERERfQxJklDNvRqquVczdBQyEdnu3Fy+fHmjn6OHiIiITFu2C58pU6ZgwIAB6NChA16/fg0A6NatG/vBEBERkdHIduEzePBgXL58Ga9evYKPjw/+/vtvLFy4kAuTEhERkdHIUefm4sWL4/Dhw5g/fz7atWuHcuXKQaHQPsSFCxd0GpCIiIhIV3I8quvBgwfYunUrHBwc8Nlnn6UpfIiIiIjyqhxVLUuXLsWoUaMQEBCAa9euwdnZObdyEZEJS1Qm4vqL6xAQ8HH2gaXC0tCRiCifyHbh06xZM5w9exbz589Hjx49cjMTEZmoZFUyJv87GXPPzkVkQiSAlAntBlcfjAkNJ8Bcbm7YgERk9LJd+KhUKly+fBkeHh65mYeITJRaqNFpcydsv7lda+XuqMQo/HryV4SEh+DvL/6GXJbx+k5ERFnJ9qiugwcPsugholyz69YubLu5TavoSaUWauy9sxdbbmwxQDIiyk9yvDq7oUyZMgW1a9eGtbU17O3t023z8OFDtGzZEtbW1nBxccG3334LpVKp36BE9EGWBC/JdLVuuSTHovOL9JiIiPIjoxmSlZSUhA4dOsDf3x/Lli1Ls1+lUqFly5Zwc3PDqVOn8OzZM/To0QNmZmb45ZdfDJCYiHLi9qvb6a7SnUolVLjz+o4eExFRfmQ0d3wmTpyIr7/+Gr6+vunuP3DgAK5fv44///wTlStXRvPmzTFp0iQsWLAASUlJek5LRDnlZO0ECZmvxu1o5ainNESUXxlN4ZOVoKAg+Pr6wtXVVbMtMDAQ0dHRuHbtmgGTEVF2dPXtmul+mSRD94rd9ZSGiPKrfFP4hIeHaxU9ADRfh4eHZ/h9iYmJiI6O1noRkf71rNwTxR2KQyFL+wReISngXtAdfav2NUAyIspPDFr4jBkzBpIkZfq6efNmrmaYOnUq7OzsNC9PT89cPR8Rpc/G3AZHex5FFbcqAFI6M6d2dq7gWgH/9voX9pb2BkxIRPmBQTs3jxo1Cr169cq0jbe3d7aO5ebmhrNnz2pti4iI0OzLyNixYzFy5EjN19HR0Sx+iAzE084TZ748g7NPzuLo/aMQEKjnVQ+1PWtDkjLv/0NElB0GLXycnZ11tuyFv78/pkyZgufPn8PFxQVAytxDtra28PHxyfD7LCwsYGFhoZMMRPTxJElCTY+aqOlR09BRiCgfMprh7A8fPsTr16/x8OFDqFQqhISEAABKliwJGxsbNG3aFD4+PujevTt+++03hIeH48cff8SQIUNMprCJS45D0KMgJKmSUNG1IorYFjF0JCIiojxFEkKknSY1D+rVqxdWrVqVZvuRI0fQsGFDACkrxw8aNAhHjx5FgQIF0LNnT0ybNi1HK8hHR0fDzs4OUVFRsLW11VX8XKVSqzDp30mYFTQL0UkpnbMlSPis7GdY2HIh3GwyftRHRESUH2T389toCh99McbC58udX2L5xeVppvqXS3J42nnifL/zcLJ2MlA6IiKi3Jfdz+98M5zdVAU/Dcayi8vSXd9IJVR4FPUIs0/PztUMCcoEXHx2ESHhIUhScbJIIiLKu1j4GLkVISvSnfcklUqosOTCklw5d6IyEd8f+h5uM9xQdUlVVFlcBYX/Vxg/H/sZSjXXSCMiorzHaDo3U/oeRz/Ossh4HvscaqGGTNJdnatUK9FmfRscuHcAaqHWbH8d/xoTjk7A1edXsb79ep2ek4jI1MUlxyE+OR72lvaQyzJe1Jcyxk8lI+ds7ZzpHR8AsLew13kBsunaJuy7u0+r6EklILDp+ibsu7NPp+ckIjJVJx+eRIu1LWDziw0KTS8E1xmu+PHwj4hJjDF0NKPDwsfIda/UPdM7PnJJjl6Ve+n8vIuDF2daTMklOZYE584jNiIiU7L1xlbUX1kfB+4e0PTnfBX/CtNOTEO9FfUQncillnKChY+Rq+dVD61KtUq3CJFLcthb2mNU7VE6P+/tV7fTvduTSiVUuPXqls7PS2Ts/rn3Dz7961M4/uqIQr8VQret3XD+6flcP++Zx2fQeXNn2E2zg80vNghYHYC/Q/8GB/bmbTGJMei+rTuEEFAJldY+lVDh6vOrmPLvFAOlM04sfIycJEnY2GEjelXqpVnXKFVlt8o42eckPGw9dH5eRyvHzHNBgpMVh9ATvWvi0Yn4ZM0n2Hd7H94kvMGr+FfYcG0DaiytgdWXVufaeVeGrIT/Mn9subEF0YnRiE2OxdH7R9F6fWuM/md0rp2XPt5fV/9CfHJ8uiN3gZTiZ3HwYo6ozQEWPvmAlZkVln22DI9HPsaqNquwpNUSnO93Huf7n0eZQmVy5ZzdKnbLst9Qt4rdcuXcRMbon3v/YMKxCQAApfjv8bRSrYSAQO8dvXHn9R2dn/fem3vou7MvBITWY/HUuwfTT03H7lu7dX5e0o2rz69m2Y8zKjEKEW8j9JTI+LHwyUfcbNzQo1IP9PPrBz93v1w9Vz+/fnCzcUtzlwkAFDIFijsUZ+FD9I65Z+Zm+gEmQcKi84t0ft7F5xdDQsYLvMolOeacmaPz85JuWJtZZ3i3511WZlZ6SJM/sPAxEVEJUZh3Zh46b+6ML7Z8gaXBSxGbFPvBx3O0csS/vf6Fj3PKArBySa4pgqq4VcGxXsdQwLyATrIT5QcnH53MdCCCSqhw4uEJnZ836HFQmr4h75/3zJMzOj8v6Ubbsm0zfd/IJBlqe9RGIetCekxl3DiPjwk4HHYYn63/DLFJsZCklN/81l9dj7GHxmJv172oXqT6Bx23hGMJXBp4CScfncTxB8chSRIaFWuEGkVqaM5DRCnSuzv6PjOZmc7PaybP+phZPUohw6lRpAYaFmuI4w+Op1vAqoUaP9b/0QDJjBfv+ORzYW/C0GpdK8Qlx0FAQC3UmtFYkQmRaPpnU7yIffHBx5ckCXW96mJsvbEYU3cManrUZNFDlI4WpVpkWmDIJBmalWym8/M2L9k80/54CpkCLUu11Pl5STckScLWjltR27M2gJQ/L4VMAZkkg5nMDH98+geal2pu4JTGhYVPPjf/7HwkqZLSHXquEipEJ0Zj2cVlBkhGZFpG1ByR4RQQMkkGK4UVvqz6pc7P26dKHxQ0L5hh8aMWanxV6yudn5d0x8HKAcd6HcO/vf7F4GqD0aNiD/wa8CuejHyCvlX7Gjqe0eHq7O8xxtXZM1N8TnHcj7yfaZsaRWrgzJd8xk+U29ZdWYce23oA+G9UVWrRs6vLLjQs1jBXznv68Wk0+7MZohOjNR1l5ZIckiRhVZtV6OLbJVfOS6RP2f385oPdfC5RmZhlm/jkeD0kyZ7X8a/xJPoJnKyd4F7Q3dBxiHSqi28X+Hv4Y3HwYhx/cBwKmQKBJQPxZdUv4VLAJdfOW8ujFsJGhGHVpVXYd2cfktXJ8PfwR3+//vCy88q18xLlRbzj8578dsfn03WfYt+dfVrzhrxLIVOge8XuWP7Zcq3tEW8jcOPlDVibWaNq4aq53vnxzus7+P7Q99h6Y6vmN+F6XvUwufFk1C9aP1fPTURExi+7n9/s45PPDa0xNMOiB0iZPG1w9cGar59EP0GHjR1QZGYRNFrVCDX/qAnPWZ5YcHZBrk1tf+vVLdRYWgPbbm7TGrVw8tFJNF7VGHtu78mV8xIZsxsvbuDA3QMICQ/hshNEOcDCJ59rWqIpRtQcAQBanRtTh9ZObjQZ1dyrAUi5y1NrWa00BUj423AM3TsU446My5WMX+37CtGJ0WnmqkgdgdZ7R28kq5Jz5dxExubUo1OosbQGfH73QeCfgaiyuAp8fvfh7MtE2cTCJ5+TJAmzAmfhr8//gl/hlNmcJUio41UHOzvvxA/1f9C0nXZiGp7FPMtwsrMpx6cg7E2YTvM9jn6MfXf2ZXhOAYHnsc+x985enZ6XyBidfHgSDVc2RPCzYK3toS9D8elfn2Lrja0GSkZkPNi52QRIkoTOFTqjc4XOUKqVkCBBLtOeTE2pVmLZxWWZzvAqk2RYdWkVJjScoLNs997cy3I6drkkx+1Xt3V2TiJjNWzvMKiEKs2weAEBCRKG7BmC1mVac0JCokzwjo+JUcgUaYoeAIhOjEZMUkym3ytJEh5EPdBpHjsLuyzbqIQKdpZZt9MnpVqJFRdXoNqSaijwSwG4THfB0D1Dc2WRScp9Qghsub4FDVc2RMGpBeH0mxP67OiDKxFXDB1N4+rzq7gYfjHDuYAEBMLfhuPg3YN6TkZkXFj4EADAxtwmW9PlO1k56fS8FV0rooRDiUwXUVTIFPiszGc6Pe/HSFYlo+36tuizsw8uhl9EXHIcXsS9wOLgxai4sCKOPzhu6IiUA0IIDNw9EO03tceJhyfwNuktXse/xprLa1B1SVXsuLnD0BEBAA8is/dLh65/OSHKb1j4EADAXG6ODuU7ZHqLXKlW6nyiM0mSMLnx5Awfd0mQMLzGcDgXcNbpeT/GrNOzsPt2SkfSd3/7VqqVSFQlou2GtkhQJhgqHuXQuivrsCR4CQBoPepVqpVQqVXotLnTRy3roivZ/TvgbJ13/q58jCRVEtZdWYfANYHwXeiLVutaYduNbVCpM34cT5QdLHxI44d6P8Bcbp7uYooySYbPy32OqoWr6vy8nSt0xqKWi2ClsIIECWYyM8gkGWSSDENrDMVvn/ym83N+KLVQY86ZORkWamqhxqv4V9h0bZOek9GHmn1mdobLOQgIJKuTsfzi8nT361M192rwdvDO9O6orYUtWpRqocdUuSMyIRJ1ltVB161d8U/YP7j6/Cr23dmHdhvbIfDPwDw16SoZHxY+pOHj7IPDPQ6jqH1RACnFjgQJMkmGXpV64c92f+bauQdUG4Dwb8KxuNVifFP7G0z/ZDoefPUAc5vPTbdPkqFEvI3A05inmbYxk5nh7JOzekpEH0Mt1Ljw7EKG/WaAlEdhZ54YfkkXmSTD9E+mZzoYYFKjSbAys9Jjqtzx5c4vcTH8IoD/7qqm3o07cv8IRh0YZbBsZPzY9Z+01PSoidvDbuNI2BFcfX4VVmZWaFmqJYrYFsn1c9ta2KKfX79cP8/HyM5oGQHBUTVGIrWwz6zwkSQpz/x5tivXDmvbrcXwvcPxKv4VJEgQELAxt8HkRpMxrMYwQ0f8aA+jHmLrja2Z3lVdfnE5pjSeAgcrBz2no/wgb/xtpjxFJsnQxLsJmng3MXSUPKeQdSH4uvji2vNrUCP9D0ulWonAkoF6TkYfQpIkfOL9CQ7cPZDhVA5qoUZgibzz59nFtwva+7TH3tt78Sj6EVwKuKBlqZYoYF7A0NF04tj9Y1lOcZGoSsTpx6fRvFRzPaWi/ISFD1EOSJKEMXXHoOvWrunuV0gKlHQqiaYlmuo5GX2ob2t/m+EEmXJJDkcrR3Su0FnPqTJnLjfHZ2XzzkhHXcrs7tuHtCN6H/v46MHj6Mf48/KfWBWyCqEvQw0dhz5SF98uGFc/ZfmO1EcgqZ1jPew8sLfr3gw7y1Le06h4IyxosQAyyDQd+6X//5+DlQMOdj+Yb+6mGAN/T/8s2yhkClQvUl0PaSg/4urs79Hl6uwxiTHo/3d/bLy+Ueu3kybFm2B129VwL+j+sXHJgC5HXMaS4CW4HHEZtha2aO/THp3Kd8oXnUtN0e1Xt7Ho/CKce3oOlgpLtC7TGt0rds9zk2eagqZrmuJw2OF0Hz/KJTm6+HbB6rarDZCM8rLsfn6z8HmPrgofpVqJRqsaIehRUJq/vAqZAp62nrgw4ALsLe0/MjERUfrikuNwKfwSBAQqulaEjbmNoSNlS/jbcNRbUQ93X98F8N+SHABQ2a0yDvc8zH87KY3sfn7zfnwu2Rm6Eycenkj3NxalWokHUQ+w+PxiAyQjovwuSZWE0QdHw3WGK2ovr406y+vAbYYbRu0fZRSTa7rZuCG4fzBmBs6Er4svnK2dUbVwVSxsuRAn+5xk0UMfxSgKn/v376Nv374oXrw4rKysUKJECYwfPx5JSUla7S5fvox69erB0tISnp6e+O03w018t+rSqnQnAkyVOiSTiEiXVGoV2q5vixlBM/A26a1me2xyLGafmY1W61pBqVYaMGH22FrY4qtaX+HSoEt4/u1znO9/HgOqDeCjZPpoRlH43Lx5E2q1GosXL8a1a9cwa9YsLFq0CN9//72mTXR0NJo2bYqiRYsiODgY06dPx4QJE7BkyRKDZH4W8yzTlc4BICI2Qk9piMhU7AjdgT139qQ76kkt1DgUdogzi5NJM4rh7M2aNUOzZs00X3t7eyM0NBQLFy7EjBkzAABr165FUlISli9fDnNzc5QvXx4hISGYOXMm+vfvr/fMXnZeuPDsQobFjwQJHrYeek5FRPnd0uClkEvyDP/tkUtyLA5ejC98v9BzMqK8wSju+KQnKioKjo6Omq+DgoJQv359mJuba7YFBgYiNDQUb968yfA4iYmJiI6O1nrpQp8qfbK849Ovat6epZiI8rZbr25hwN8DYDfNDmaTzFBufjkEPwvO9N8elVDh3pt7ekxJlLcYZeFz584dzJs3DwMGDNBsCw8Ph6urq1a71K/Dw8MzPNbUqVNhZ2eneXl6euokY7OSzdC8ZPN053ORS3L4OPugb9W+OjkXEZmeEw9PoPKiylgeshzRidFQqpUIfRWKF3FZryRfyLqQHhIS5U0GLXzGjBkDSZIyfd28eVPre548eYJmzZqhQ4cO6Nfv4++YjB07FlFRUZrXo0ePPvqYQMqEdls7bcXg6oNhIbfQbJdLcrT3aY9/e/9rNENLiShvSVIlod2GdkhUJWp1VM5qqQcg5TF7z0o9czMeUZ5m0D4+o0aNQq9evTJt4+3trfnvp0+folGjRqhdu3aaTstubm6IiNDuLJz6tZubW4bHt7CwgIWFRYb7P4alwhLzms/DpEaTEPQoCEq1EtXcq6FwwcK5cj4iMg3bbmzL1p2d96XOIda7Su9cSEVkHAxa+Dg7O8PZ2TlbbZ88eYJGjRrBz88PK1asgEymfbPK398fP/zwA5KTk2FmZgYAOHjwIMqUKQMHB8Ou4Gtvac/F9IhIZ84/PQ8zmRmS1clZtk193K4WalR3r44N7TfA1uLjZqUnMmZGMarryZMnaNiwIYoWLYoZM2bgxYv/ftNJvZvTpUsXTJw4EX379sXo0aNx9epVzJkzB7NmzTJUbCKiXGEuN8/WY619Xffh5subEBCoX7Q+qhauqod0RHmbURQ+Bw8exJ07d3Dnzh14eGgPAU9dccPOzg4HDhzAkCFD4Ofnh0KFCmHcuHEGGcpOlF9ceHYBO27uQFxyHHxdfdHBpwMnkMsDmpdqjl9O/JLhfgkSyhQqg6YlmiKwZKAekxHlfVyr6z26XKSUyFhFJkSi46aOOHjvIBQyBSRISFYnw87CDus+X4cWpVoYOqJJE0Kg1rJauPDsQoazMK9qswo9KvXQczIiw+FaXUQfKOxNGBafX4x5Z+bh9OPTMLXfDYQQ+Gz9ZzgcdhhAytpyqX1JohOj8dn6z3DuyTlDRjR5kiRhR+cdKONUBgA0y+MoZCk38cfVH8eihygDRvGoi0gfYhJj0HdnX2y+vlmzTUCgkmslrG+/HmULlTVgOv05/vA4/n3wb7r7BASEEPjlxC/Y1mmbnpPRu9xs3HBxwEXsCN2BTdc3IToxGmWdyqKfXz/4OPsYOh5RnsVHXe/hoy7TpBZqNFrVCCcfnkwz661cksPe0h6XBl5CEdsiBkqoP8P2DMOi4EWZLmQpk2SI+z4OForcmQqCiCin+KiLKAf239mPfx/8m+5U/yqhQmRCJOacmWOAZPoXkxSTZRu1UCNeGa+HNEREusXChwjA2itrNf0k0qMSKqwMWan5+kXsC9x5fQexSbF6SKdfZZzKpLuy97ucrJw4FwwRGSUWPkRIKWSyWlT2TcIbHL1/FA1WNoDLDBeUmlcKhaYXQv+/+yP8bcbrwRmbXpV7QYKU4X65JMegaoPSXYeOiCiv479cRACK2RfTjIjJiIOlA5qsboITD09otiUoE7Di4grUWFoDz2Ke5XZMvShcsDBmN5sNAGmKm9QFdr+t860BkhERfTwWPkQA+lTpk2Vn3ujEaAgh0jwGUgolnr19hu8Pf5/bMfVmaI2h2NpxKyq6VtRsszG3wbAaw3C893E+5iIio8VRXe/hqC7TJITAl39/iRUXV6RZCkAuyeFm44YnMU8yPYa53BzPv3kOO0u73Iyqd0+inyBeGQ8PWw9YKiwNHYeIKF0c1UWUA5IkYUmrJfi50c+wt7TXbFfIFOji2wWdy3eGmcws02MkqZLwMOphLifVvyK2RVDSsSSLHiLKFziBIdH/k8vk+LH+j/i29rc4//Q8klRJ8HX1RSHrQvjt5G9ZjnQCwEdARER5HO/4EL3HQmGBOl510Kh4IxSyLgQAaFeuXaajvmSSDFXcqqCofVF9xSQiog/AwocoG0o6lkSXCl0yHMKtFmpMbDhRz6mIiCinWPgQZdOyz5aho09HACkdns1kZpAgwVJhieWtl+PTMp8aOCEREWWFo7rew1FdlJUbL25g0/VNiEqISrkT5Nsl343kIiIyNtn9/Gbh8x4WPkRERMaHw9mJiIiI3sPh7EYuNikWpx6dQpIqCZXcKsHD1sPQkYiy9Cb+Dc49PQcJEqq5V4ODlUOOvv9B5ANcfX4VlgpL1PasDSszq1xKSkT5DQsfI6VUKzHh6ATMOTMHb5PeAgAkSGhdpjUWtVoENxs3AyckSis2KRajDozCypCVSFQlAgAs5BboXaU3/tf0f7A2s870+x9FPcLAXQOx985ezQzbtha2+Mb/G/xQ/wcunEpEWWIfn/cYQx8fIQR6be+FNZfXpFleQSFTwNPWE+f7n4ejlaOBEhKllaxKRuPVjXHq0ak0k0HKJTnqeNXBP93/gZk8/RmyI95GwG+JH8Lfhqc7p9LAagOxsOXCXMlORHkf+/jkY+eensPqy6vTFD1Ayp2gh1EPMef0HAMkI8rYxmsbceLhiXRnwFYJFf598C82X9+c4fdPPzU9w6IHABadX4Srz6/qLC8R5U8sfPKQW69uYfDuwXD6zQlWU6zgt8QPyy8uT7Nq+IqLK6CQZfyUUiVUWHJhSW7HJcqRpReWZvooSi7JsTh4MdK7CS2EwB8X/sh09myFTIEVF1foJGt+plQrkaRKMnQMIoNh4ZNHHL1/FJUWVcLSC0vxOv41EpQJCAkPQd+dfdF2fVskq5I1bR9HP05TDL0v4m1Euh8gRIZyP/J+puudqYQKxx4cQ4FfCuDLnV/i1qtbmn0JygREJUZleny1UONxzGOd5c1v9t7ei0arGsF8kjksJlvAd6Evll9cnq016IjyExY+eUB8cjzabWiHJFWSVkGT+g/S7tu7Mfv0bM12lwIumd7xAQAHKwdIkpQreYk+hKuNKyRk/Z6MV8Zj1aVVqLq4Ks4+OQsAsFRYZtnxWSbJ4GLtopOs+c3MoJlosa4Fjj84rnlEfu35NfTd2Rd9d/TlL0lkUlj45AEbr23Em4Q3Gf7mJSAw58wczf7ulbpnesdHLsnRp3KfXMlK9KF6V+6d7bZKtRIJygR02NQBaqGGJEnoWalnpgW/Uq1Ej0o9dBE1X7nx4gZGHRgFAFqPClMLoJWXVmbat4oov2HhkwecfXIWZrL0R7KkehLzBC9iXwAAGhRtgBYlW6TbX0IuyeFo5Yiv/b/OlaxEH6pHpR4oW6gs5JI8W+1VQoWHUQ9x4O4BAMDoOqNR0Lxgut8vk2Ro79Me1YtU12nm/GDR+UWZFoxySY55Z+fpMRGRYbHwyQMUMkW6I7TelzrMV5IkbO64Gb0r907zD5qfux9O9jkJ94LuuZKV6ENZm1njaK+jCPAOyPb3KGQKXHx2EQBQ1L4oTvQ5gYquFdO0GVhtIP5s+2eWxwsJD8GgXYNQb3k9tFjbAssuLENcclzOfhAjc+HZhUzvEKuECiHhIfoLRGRgnMAwDwgsGYi5Z+dmuF8myVDJtZLWvDxWZlb4o/UfmNx4Mv659w8SlYnwc/dDZbfKekhM9GFcCrhgX7d9CH0Zir+u/oWJxyZm2l4t1LBUWGq+9nH2wYUBF3D+6XlcCr8ES4UlmpZoCucCzpkeRwiB8UfHY9K/k6CQFFAKJWSSDHvv7MWkfyfhSM8jKO5QXCc/Y15jZWYFCVKmv1xZKCz0mIjIsDiB4XsMMYGhSq1ChYUVcOfVHShF+r+ZbWi/AR3Ld9RLHiJ9UKlVKDq7KJ7EPMm0XejQUJR2Kv1R51p7eS26beuW7j6FpEAJxxK4PuR6vpz5ecHZBRi2d1iGhY9CpkDfKn2xqNUiPScj0i1OYGhE5DI59nbdCw+7lHW2ZP//x5L6GOvnhj+z6KF8Ry6T4/t632e8X5LjszKffXTRI4TAtJPTNH+v3qcUSoS+CtX0JcpvulfqDucCzun2jZIgQSbJMLzmcAMkIzIMFj55RDH7Yrg++DpWtVmFlqVbomHRhhhUbRCuDrqKnxr8ZOh4RLliULVBGFNnDICUQl+CpCn46xWth9VtV3/0OV7GvcTV51ehRsbz1ZjJzLDvzr6PPldeZGthi8M9DsPVxhVASkEpk2SQIMHKzArbO22Hj7OPgVMS6Y/RPOpq3bo1QkJC8Pz5czg4OCAgIAC//vor3N3/68R7+fJlDBkyBOfOnYOzszOGDRuG7777LkfnMYa1uojym9CXoVh2cRnuvrkLR0tHdPHtgobFGupkLqpnMc/gPjPzzv5mMjP09+uP+S3mf/T58qoEZQI2X9+MA3cPQKlWomaRmuhZuSfsLe0NHY1IJ7L7+W00hc+sWbPg7++PwoUL48mTJ/jmm28AAKdOnQKQ8gOXLl0aAQEBGDt2LK5cuYI+ffpg9uzZ6N+/f7bPw8KHKH9RCzW8Znll2ZdoTds16FYx/X5ARJT35bvC5307d+5EmzZtkJiYCDMzMyxcuBA//PADwsPDYW5uDgAYM2YMtm/fjps3b2b7uCx8iPKf6SenY/Q/o9Pt4CuTZHCwdMDjkY+1RpARkXHJ152bX79+jbVr16J27dowM0uZ2yYoKAj169fXFD0AEBgYiNDQULx588ZQUYkoD/iq1lf4tPSnAKA1ckshKWCpsMT2zttZ9BCZCKMqfEaPHo0CBQrAyckJDx8+xI4dOzT7wsPD4erqqtU+9evw8PAMj5mYmIjo6GitFxHlL2ZyM2zttBUrP1sJv8J+sDGzgUsBFwyqPgiXB15GXa+6ho5IRHpi0MJnzJgxkCQp09e7j6m+/fZbXLx4EQcOHIBcLkePHj0+enG9qVOnws7OTvPy9PT82B+LiPIguUyOnpV74my/s4j5PgYR30RgbvO5KOFYwtDRiEiPDNrH58WLF3j16lWmbby9vbUeX6V6/PgxPD09cerUKfj7+6NHjx6Ijo7G9u3bNW2OHDmCxo0b4/Xr13BwcEj3+ImJiUhMTNR8HR0dDU9PT/bxISIiMiLZ7eNj0CUrnJ2d4eyc+VTzGVGrU+bkSC1a/P398cMPPyA5OVnT7+fgwYMoU6ZMhkUPAFhYWMDCgtO1ExERmQKj6ONz5swZzJ8/HyEhIXjw4AEOHz6ML774AiVKlIC/vz8AoEuXLjA3N0ffvn1x7do1bNiwAXPmzMHIkSMNnJ6IiIjyCqMofKytrbF161Y0adIEZcqUQd++fVGxYkUcO3ZMc7fGzs4OBw4cQFhYGPz8/DBq1CiMGzcuR3P4EBERUf5mtPP45BbO40NERGR88vU8PkREREQfgoUPERERmQwWPkRERGQyWPgQERGRyWDhQ0RERCaDhQ8RERGZDBY+REREZDJY+BAREZHJYOFDREREJoOFDxEREZkMFj5ERERkMlj4EBERkclg4UNEREQmg4UPERERmQwWPkRERGQyFIYOQJTXqYUau27twtLgpbj35h5cbFzQvWJ3fFHhC1iZWRk6HhER5YAkhBCGDpGXREdHw87ODlFRUbC1tdXpsdVCjYN3D2JH6A7EJcfB18UXPSv3RCHrQjo9D+lOojIRn2/8HLtv74ZckkMlVJBJMqiFGuWdy+Nwz8NwKeBi6JhERCYvu5/fLHzek1uFT/jbcDRf2xwh4SFQyFJutKmFGgqZAstbL0fXil11di7SnW8PfIuZp2dCLdRp9sklORoVa4SDPQ4aIBkREb0ru5/f7OOjB2qhRvO1zXH1+VUAgFKthFKthFqokaRKQvdt3XHs/jEDp6T3xSbFYuH5hekWPQCgEir8E/YPrr+4rudkRET0oVj46MHBuwcREh4CpVqZ7n6ZJMPUE1P1nIqycuHZBcQmx2baRoKEI2FH9JSIiIg+FgsfPdgRukPzeCs9KqHCgbsHkKBM0GMqyopA9p4CZ7cdEREZHgsfPYhLjsuyjYBAojJRD2kouyq7VYalwjLTNgICdb3q6ikRERF9LBY+euDr4pthP5FUhW0Kw9ZCt6PIdOnu67s48fAE7ry+Y+goemNrYYu+VfpCLsnT3a+QKVDbozYqu1XWbzAiIvpgLHz0oGflnpk+6pJJMgyrMQySJOkxVfacenQK/sv8UXJeSdRbUQ+l5pVCrT9q4cTDE4aOphe/ffIb/D39AaT8OQEp/XokSPCw9cD69usNGY+IiHKIhY8eFLIuhOWtl0OClObugUySobZnbXzt/7WB0mXs2P1jaLiyIc4+Oau1/dzTc2i0qhGO3j9qmGB6ZG1mjUM9DmHlZytRs0hNuNm4oYJLBcxoOgMhA0Lgaedp6IhERJQDnMfnPbk5geGx+8cw9cRUHLh7AAIC7gXdMbT6UHzt/3WWfUn0TQiBcgvK4fbr2+k+ppNBhhKOJRA6NDRP3qkiIiLTkt3Pby5ZoUcNijVAg2INkKBMQKIyEbYWtnm2aDjz5AxCX4VmuF8NNW6/vo3Tj09rHgURERHldXzUZQCWCkvYWdrl2aIHAO5H3s9Wu7DIsNwNYkBCCOy+tRuBfwbC4VcHuEx3Qd+dfXEl4oqhoxER0Qdi4UPpcrRyzFY7JyunXE5iGEIIjNw/Eq3+aoVD9w4hMiESL+JeYPWl1ai6pCq23dhm6IhERPQBWPhQuhoWa5jl4qlOVk5oVLyRnhLp17ab2zD7zGwAKRNMplKqlVCpVei8pTPC34YbKB0REX0oFj6ULnO5OX5p/EumbaY0ngJzubmeEunX7NOzM5y/R0BAqVZi2YVlek5FREQfi4UPZaifXz/Maz4PBcwKAICmELA2s8acZnMwoNoAQ8bLVacfn9a60/M+tVDj1ONTekxERES6YHSFT2JiIipXrgxJkhASEqK17/Lly6hXrx4sLS3h6emJ3377zTAh85GhNYYi/JtwrGm7Br80+QWr26xGxDcRGF5zuKGj5Sq5LP27PakkSDCTmekpDRER6YrRDWf/7rvv4O7ujkuXLmltj46ORtOmTREQEIBFixbhypUr6NOnD+zt7dG/f38Dpc0fbMxt0K1iN0PH0KumJZpiz609UAplhm0CvAP0mIiIiHTBqO747N27FwcOHMCMGTPS7Fu7di2SkpKwfPlylC9fHp07d8bw4cMxc+ZMAyQlYzfKf1SGRY9MksHe0h49KvXQcyoiIvpYRlP4REREoF+/flizZg2sra3T7A8KCkL9+vVhbv5fZ9vAwECEhobizZs3GR43MTER0dHRWi+i+kXrY2HLhZBBBoX0341RmSSDrYUt9nXbl6cXlSUiovQZReEjhECvXr0wcOBAVKtWLd024eHhcHV11dqW+nV4eMbDjqdOnQo7OzvNy9OTay9RioHVBuL6kOsYVnMYannUQoOiDfBbwG+4M+wOahSpYeh4RET0AQzax2fMmDH49ddfM21z48YNHDhwADExMRg7dqzOM4wdOxYjR47UfB0dHc3ihzTKFCqDmYF8XEpElF8YtPAZNWoUevXqlWkbb29vHD58GEFBQbCwsNDaV61aNXTt2hWrVq2Cm5sbIiIitPanfu3m5pbh8S0sLNIcl4iIiPIngxY+zs7OcHZ2zrLd3LlzMXnyZM3XT58+RWBgIDZs2ICaNWsCAPz9/fHDDz8gOTkZZmYpw4wPHjyIMmXKwMHBIXd+ACIiIjIqRjGc3cvLS+trGxsbAECJEiXg4eEBAOjSpQsmTpyIvn37YvTo0bh69SrmzJmDWbNm6T0vERER5U1GUfhkh52dHQ4cOIAhQ4bAz88PhQoVwrhx4ziHDxEREWlIQghh6BB5SXR0NOzs7BAVFQVbWw5XJiIiMgbZ/fw2iuHsRERERLrAwoeIiIhMBgsfIiIiMhksfIiIiMhksPAhIiIik5FvhrPrSuogNy5WSkREZDxSP7ezGqzOwuc9MTExAMD1uoiIiIxQTEwM7OzsMtzPeXzeo1arERoaCh8fHzx69Ihz+WQidUFXXqfM8TplD69T9vA6ZQ+vU/bkp+skhEBMTAzc3d0hk2Xck4d3fN4jk8lQpEgRAICtra3RvxH0gdcpe3idsofXKXt4nbKH1yl78st1yuxOTyp2biYiIiKTwcKHiIiITAYLn3RYWFhg/PjxsLCwMHSUPI3XKXt4nbKH1yl7eJ2yh9cpe0zxOrFzMxEREZkM3vEhIiIik8HCh4iIiEwGCx8iIiIyGSx8iIiIyGSYbOGzcOFCVKxYUTNpk7+/P/bu3avZn5CQgCFDhsDJyQk2Njb4/PPPERERYcDEecO0adMgSRK++uorzTZeK2DChAmQJEnrVbZsWc1+XqP/PHnyBN26dYOTkxOsrKzg6+uL8+fPa/YLITBu3DgULlwYVlZWCAgIwO3btw2YWP+KFSuW5v0kSRKGDBkCgO+nVCqVCj/99BOKFy8OKysrlChRApMmTdJaq4nvpxQxMTH46quvULRoUVhZWaF27do4d+6cZr9JXSdhonbu3Cl2794tbt26JUJDQ8X3338vzMzMxNWrV4UQQgwcOFB4enqKQ4cOifPnz4tatWqJ2rVrGzi1YZ09e1YUK1ZMVKxYUYwYMUKznddKiPHjx4vy5cuLZ8+eaV4vXrzQ7Oc1SvH69WtRtGhR0atXL3HmzBlx7949sX//fnHnzh1Nm2nTpgk7Ozuxfft2cenSJdG6dWtRvHhxER8fb8Dk+vX8+XOt99LBgwcFAHHkyBEhBN9PqaZMmSKcnJzErl27RFhYmNi0aZOwsbERc+bM0bTh+ylFx44dhY+Pjzh27Ji4ffu2GD9+vLC1tRWPHz8WQpjWdTLZwic9Dg4O4o8//hCRkZHCzMxMbNq0SbPvxo0bAoAICgoyYELDiYmJEaVKlRIHDx4UDRo00BQ+vFYpxo8fLypVqpTuPl6j/4wePVrUrVs3w/1qtVq4ubmJ6dOna7ZFRkYKCwsL8ddff+kjYp40YsQIUaJECaFWq/l+ekfLli1Fnz59tLa1a9dOdO3aVQjB91OquLg4IZfLxa5du7S2V61aVfzwww8md51M9lHXu1QqFdavX4/Y2Fj4+/sjODgYycnJCAgI0LQpW7YsvLy8EBQUZMCkhjNkyBC0bNlS65oA4LV6x+3bt+Hu7g5vb2907doVDx8+BMBr9K6dO3eiWrVq6NChA1xcXFClShUsXbpUsz8sLAzh4eFa18rOzg41a9Y0uWuVKikpCX/++Sf69OkDSZL4fnpH7dq1cejQIdy6dQsAcOnSJZw4cQLNmzcHwPdTKqVSCZVKBUtLS63tVlZWOHHihMldJ5NepPTKlSvw9/dHQkICbGxssG3bNvj4+CAkJATm5uawt7fXau/q6orw8HDDhDWg9evX48KFC1rPg1OFh4fzWgGoWbMmVq5ciTJlyuDZs2eYOHEi6tWrh6tXr/IavePevXtYuHAhRo4cie+//x7nzp3D8OHDYW5ujp49e2quh6urq9b3meK1SrV9+3ZERkaiV69eAPh37l1jxoxBdHQ0ypYtC7lcDpVKhSlTpqBr164AwPfT/ytYsCD8/f0xadIklCtXDq6urvjrr78QFBSEkiVLmtx1MunCp0yZMggJCUFUVBQ2b96Mnj174tixY4aOlac8evQII0aMwMGDB9P8tkD/Sf0NEwAqVqyImjVromjRoti4cSOsrKwMmCxvUavVqFatGn755RcAQJUqVXD16lUsWrQIPXv2NHC6vGnZsmVo3rw53N3dDR0lz9m4cSPWrl2LdevWoXz58ggJCcFXX30Fd3d3vp/es2bNGvTp0wdFihSBXC5H1apV8cUXXyA4ONjQ0fTOpB91mZubo2TJkvDz88PUqVNRqVIlzJkzB25ubkhKSkJkZKRW+4iICLi5uRkmrIEEBwfj+fPnqFq1KhQKBRQKBY4dO4a5c+dCoVDA1dWV1yod9vb2KF26NO7cucP30zsKFy4MHx8frW3lypXTPBZMvR7vj1AyxWsFAA8ePMA///yDL7/8UrON76f/fPvttxgzZgw6d+4MX19fdO/eHV9//TWmTp0KgO+nd5UoUQLHjh3D27dv8ejRI5w9exbJycnw9vY2uetk0oXP+9RqNRITE+Hn5wczMzMcOnRIsy80NBQPHz6Ev7+/ARPqX5MmTXDlyhWEhIRoXtWqVUPXrl01/81rldbbt29x9+5dFC5cmO+nd9SpUwehoaFa227duoWiRYsCAIoXLw43NzetaxUdHY0zZ86Y3LUCgBUrVsDFxQUtW7bUbOP76T9xcXGQybQ/xuRyOdRqNQC+n9JToEABFC5cGG/evMH+/fvx2Wefmd51MnTvakMZM2aMOHbsmAgLCxOXL18WY8aMEZIkiQMHDgghUoaLenl5icOHD4vz588Lf39/4e/vb+DUecO7o7qE4LUSQohRo0aJo0ePirCwMHHy5EkREBAgChUqJJ4/fy6E4DVKdfbsWaFQKMSUKVPE7du3xdq1a4W1tbX4888/NW2mTZsm7O3txY4dO8Tly5fFZ599lm+H1WZGpVIJLy8vMXr06DT7+H5K0bNnT1GkSBHNcPatW7eKQoUKie+++07Thu+nFPv27RN79+4V9+7dEwcOHBCVKlUSNWvWFElJSUII07pOJlv49OnTRxQtWlSYm5sLZ2dn0aRJE03RI4QQ8fHxYvDgwcLBwUFYW1uLtm3bimfPnhkwcd7xfuHDayVEp06dROHChYW5ubkoUqSI6NSpk9bcNLxG//n7779FhQoVhIWFhShbtqxYsmSJ1n61Wi1++ukn4erqKiwsLESTJk1EaGiogdIazv79+wWAdH92vp9SREdHixEjRggvLy9haWkpvL29xQ8//CASExM1bfh+SrFhwwbh7e0tzM3NhZubmxgyZIiIjIzU7Del6yQJ8c4Ul0RERET5GPv4EBERkclg4UNEREQmg4UPERERmQwWPkRERGQyWPgQERGRyWDhQ0RERCaDhQ8RERGZDBY+RJRvHD16FJIkpVnHKruKFSuG2bNnZ7v9ypUr06yS/iEkScL27ds/+jhElDUWPkSkUyqVCrVr10a7du20tkdFRcHT0xM//PBDrp27du3aePbsGezs7HLtHERk3Fj4EJFOyeVyrFy5Evv27cPatWs124cNGwZHR0eMHz8+185tbm4ONzc3SJKUa+cgIuPGwoeIdK506dKYNm0ahg0bhmfPnmHHjh1Yv349Vq9eDXNz8wy/b/To0ShdujSsra3h7e2Nn376CcnJyQAAIQQCAgIQGBiI1JV2Xr9+DQ8PD4wbNw5A2kddDx48wKeffgoHBwcUKFAA5cuXx549e7L9c8ycORO+vr4oUKAAPD09MXjwYLx9+zZNu+3bt6NUqVKwtLREYGAgHj16pLV/x44dqFq1KiwtLeHt7Y2JEydCqVRmOwcR6Q4LHyLKFcOGDUOlSpXQvXt39O/fH+PGjUOlSpUy/Z6CBQti5cqVuH79OubMmYOlS5di1qxZAFL6waxatQrnzp3D3LlzAQADBw5EkSJFNIXP+4YMGYLExET8+++/uHLlCn799VfY2Nhk+2eQyWSYO3curl27hlWrVuHw4cP47rvvtNrExcVhypQpWL16NU6ePInIyEh07txZs//48ePo0aMHRowYgevXr2Px4sVYuXIlpkyZku0cRKRDhl0jlYjysxs3bggAwtfXVyQnJ+f4+6dPny78/Py0tm3cuFFYWlqKMWPGiAIFCohbt25p9h05ckQAEG/evBFCCOHr6ysmTJiQ7fMVLVpUzJo1K8P9mzZtEk5OTpqvV6xYIQCI06dPa7al/sxnzpwRQgjRpEkT8csvv2gdZ82aNaJw4cKarwGIbdu2ZTsnEX04hUGrLiLK15YvXw5ra2uEhYXh8ePHKFasGICUOzV//vmnpl3q46MNGzZg7ty5uHv3Lt6+fQulUglbW1utY3bo0AHbtm3DtGnTsHDhQpQqVSrD8w8fPhyDBg3CgQMHEBAQgM8//xwVK1bMdv5//vkHU6dOxc2bNxEdHQ2lUomEhATExcXB2toaAKBQKFC9enXN95QtWxb29va4ceMGatSogUuXLuHkyZNad3hUKlWa4xCRfvBRFxHlilOnTmHWrFnYtWsXatSogb59+2r65vz8888ICQnRvAAgKCgIXbt2RYsWLbBr1y5cvHgRP/zwA5KSkrSOGxcXh+DgYMjlcty+fTvTDF9++SXu3buH7t2748qVK6hWrRrmzZuXrfz3799Hq1atULFiRWzZsgXBwcFYsGABAKTJlJm3b99i4sSJWj/vlStXcPv2bVhaWmb7OESkG7zjQ0Q6FxcXh169emHQoEFo1KgRihcvDl9fXyxatAiDBg2Ci4sLXFxctL7n1KlTKFq0qNZw9wcPHqQ59qhRoyCTybB37160aNECLVu2ROPGjTPM4unpiYEDB2LgwIEYO3Ysli5dimHDhmX5MwQHB0OtVuN///sfZLKU3xE3btyYpp1SqcT58+dRo0YNAEBoaCgiIyNRrlw5AEDVqlURGhqKkiVLZnlOIsp9LHyISOfGjh0LIQSmTZsGIGViwBkzZuCbb75B8+bNNY+83lWqVCk8fPgQ69evR/Xq1bF7925s27ZNq83u3buxfPlyBAUFoWrVqvj222/Rs2dPXL58GQ4ODmmO+dVXX6F58+YoXbo03rx5gyNHjmgKkqyULFkSycnJmDdvHj799FOcPHkSixYtStPOzMwMw4YNw9y5c6FQKDB06FDUqlVLUwiNGzcOrVq1gpeXF9q3bw+ZTIZLly7h6tWrmDx5crayEJEOGbqTERHlL0ePHhVyuVwcP348zb6mTZuKxo0bC7Vane73fvvtt8LJyUnY2NiITp06iVmzZgk7OzshhBDPnz8Xrq6uWh2Fk5KShJ+fn+jYsaMQIm3n5qFDh4oSJUoICwsL4ezsLLp37y5evnyZYfb3OzfPnDlTFC5cWFhZWYnAwECxevVqreOvWLFC2NnZiS1btghvb29hYWEhAgICxIMHD7SOu2/fPlG7dm1hZWUlbG1tRY0aNcSSJUs0+8HOzUR6Iwnx/w/diYiIiPI5dm4mIiIik8HCh4iIiEwGCx8iIiIyGSx8iIiIyGSw8CEiIiKTwcKHiIiITAYLHyIiIjIZLHyIiIjIZLDwISIiIpPBwoeIiIhMBgsfIiIiMhksfIiIiMhk/B/QnVhEsZOiBQAAAABJRU5ErkJggg=="
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": "<Figure size 640x480 with 1 Axes>",
            "image/png": "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"
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Team 596 has made 4 goals as indicated by red dots. The graph design implies that except one outlier goal shot, all the shots were present on the positive x coordinates\n",
            "Team 724 has made just 1 goal as indicated by red dot. The graph design implies that their shots were evently distributed over the field.\n"
          ]
        }
      ],
      "source": [
        "# Importing pandas  & matplotlib library\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Reading data from csv files to create dataframe\n",
        "df1 = pd.read_csv('Tutorial22_df.csv')\n",
        "df2 = pd.read_csv('Tutorial22_xG_df.csv')\n",
        "\n",
        "# Filtering data by team  & eventname\n",
        "T1 = df1[(df1['teamid'] == 724) & (df1[\"eventname\"] == \"shot\")]\n",
        "T2 = df1[(df1['teamid'] == 596) & (df1[\"eventname\"] == \"shot\")]\n",
        "\n",
        "# Consolidating individual team data to create a master data\n",
        "Data = [[T1[['xcoord']], T1[['ycoord']], T1[['goal']].values.tolist()],\n",
        "        [T2[['xcoord']], T2[['ycoord']], T2[['goal']].values.tolist()]]\n",
        "\n",
        "\n",
        "def scatterPlot(x, y, z, TeamNum=None, **kwargs):\n",
        "    \"\"\" This function when passed with x, y cordinates along with z value will construct a 2D scatter plot\"\"\"\n",
        "\n",
        "    # Define colors to highlight goaled shots with red\n",
        "    colors = [\"red\" if i[0] == 1 else \"green\" for i in z]\n",
        "\n",
        "    # Create scatter plot\n",
        "    plt.scatter(x, y, color=colors)\n",
        "\n",
        "    # Adding labels and scatter plot title\n",
        "    plt.xlabel(\"X-axis label\")\n",
        "    plt.ylabel(\"Y-axis label\")\n",
        "    plt.title(\"Team {} Scatter Plot\".format(TeamNum))\n",
        "\n",
        "    # Display plot\n",
        "    plt.show()\n",
        "\n",
        "\n",
        "def comments():\n",
        "    \"\"\" Comments on scatter plot\"\"\"\n",
        "\n",
        "    print('Team 596 has made 4 goals as indicated by red dots. The graph design implies that except one '\n",
        "          'outlier goal shot, all the shots were present on the positive x coordinates')\n",
        "\n",
        "    print('Team 724 has made just 1 goal as indicated by red dot. The graph design implies that their shots were '\n",
        "          'evently distributed over the field.')\n",
        "\n",
        "\n",
        "# Calling function to draw plot for the individual teams\n",
        "\n",
        "scatterPlot(x=Data[0][0], y=Data[0][1], z=Data[0][2], TeamNum=724)\n",
        "scatterPlot(x=Data[1][0], y=Data[1][1], z=Data[1][2], TeamNum=596)\n",
        "comments()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "c42be5fc",
      "metadata": {
        "id": "c42be5fc"
      },
      "source": [
        "## Q5)\n",
        "### a) If the centre of the net that teams shoot at is located at xCoord=89, yCoord=0, create a column for the distance from each shot to this point. What is the distance of the furthest goal scored in the game?\n",
        "### b) What is the expected goals (xg) value of this furthest goal and what do you think contributed to this xg value?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "7b9c6e2d",
      "metadata": {
        "id": "7b9c6e2d",
        "outputId": "12ffcc87-097f-4ca8-87d5-9fe9ab939545"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Distance of the furthest goal scored in the game is 188.38995295426992\n",
            "No corresponding xg value found!\n"
          ]
        }
      ],
      "source": [
        "# Importing pandas  & numpy library\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "# Reading data from csv files\n",
        "df1 = pd.read_csv('Tutorial22_df.csv')\n",
        "df2 = pd.read_csv('Tutorial22_xG_df.csv')\n",
        "\n",
        "\n",
        "def part_a():\n",
        "    \"\"\"\n",
        "    If the centre of the net that teams shoot at is located at xCoord=89, yCoord=0, create a column for the\n",
        "    distance from each shot to this point. What is the distance of the furthest goal scored in the game?\n",
        "    \"\"\"\n",
        "\n",
        "    # Fetching the x & y cordinates from dataframe df1\n",
        "    x = np.array(df1[['xcoord']])\n",
        "    y = np.array(df1[['ycoord']])\n",
        "\n",
        "    # Adding a new column called distance which stores distance between centre and specified coordinates\n",
        "    df1['distance'] = ((89 - x) ** 2 + y ** 2) ** 0.5   # pythagoras theorem to calc distance\n",
        "\n",
        "    # Goal data furthest from centre of the net\n",
        "    Farthest_Goal_Data = df1.loc[df1['distance'].idxmax()]\n",
        "\n",
        "    print('Distance of the furthest goal scored in the game is {}'.format(Farthest_Goal_Data[['distance']].tolist()[0]))\n",
        "    return Farthest_Goal_Data\n",
        "\n",
        "\n",
        "def part_b(Farthest_Goal_Data):\n",
        "    \"\"\"\n",
        "    What is the expected goals (xg) value of this furthest goal and what do you think contributed to this xg\n",
        "    value?\n",
        "    \"\"\"\n",
        "    # Connecting both the tables with compilegametime as a foreign key to pull out xg value of the farthest goal shot\n",
        "    compiledgametime = float(Farthest_Goal_Data[['compiledgametime']].tolist()[0])\n",
        "\n",
        "    # Storing xg value\n",
        "    xg_value = (df2[df2['xg'] == compiledgametime])\n",
        "\n",
        "    # Checking if xg value exists for that goal\n",
        "    if len(xg_value) == 0:\n",
        "        print('No corresponding xg value found!')\n",
        "    else:\n",
        "        print('The corresponding xg value for the maximum distance calculated is {}'.format(compiledgametime))\n",
        "\n",
        "\n",
        "Farthest_Goal_Data = part_a()\n",
        "part_b(Farthest_Goal_Data)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "7fd43684",
      "metadata": {
        "id": "7fd43684"
      },
      "source": [
        "## Q6)\n",
        "### a) If a \"Shot Assist\" is defined as a sequence of events with the same possessionid where there is: 1) a successful pass followed by 2) a successful reception by a teammate and then without giving up the puck 3) the receiving player has a shot attempt, create a column flagging shots that have a Shot Assist. Which player(s) had the most assisted shots in the game and how many assisted shots did they have?\n",
        "\n",
        "### Hint: This can be done using iterrows() or using shift() logic. Consider if you should include ALL event rows and beware of sorting!"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "652b0c8f",
      "metadata": {
        "id": "652b0c8f",
        "outputId": "822c3e4d-9af8-4300-c6ae-2d434d9c6506"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "The below list of players ids have the most number of assisted shots with the number being 1\n",
            "[332856, 332856, 628757, 838211, 538217, 538217, 628757, 838211, 288890, 288890, 538217, 677394, 677394, 288890, 84875, 673651, 628757, 628757, 628757, 628757, 673651, 764371, 84875, 628757, 628757, 797810, 952287, 952287, 952287, 952287, 952287, 485421, 797810, 628757, 628757, 838211, 838211, 628757, 838211, 677394, 677394, 677394, 838211, 838211, 838211, 677394, 677394, 698619, 838211, 677394, 698619, 698619, 677394, 677394, 677394, 698619, 698619, 698619, 628757, 261698, 628757, 261698, 628757, 698619, 890686, 890686, 890686, 673651, 847481, 485421, 485421, 485421, 847481, 393337, 828703, 812630, 812630, 812630, 393337, 828703, 424862, 424862, 600730, 628757, 628757, 261698, 952287, 952287, 952287, 511560, 797810, 797810, 952287, 511560, 332856, 890686, 890686, 538217, 538217, 154967, 332856, 332856, 628757, 154967, 154967, 84875, 698619, 831664, 183489, 698619, 698619, 698619, 698619, 764371, 84875, 698619, 831664, 183489, 485421, 485421, 485421, 915333, 45223, 915333, 485421, 45223, 485421, 915333, 485421, 45223, 485421, 828703, 828703, 828703, 828703, 485421, 812630, 828703, 828703, 485421, 485421, 915333, 485421, 485421, 812630, 485421, 915333, 511560, 815413, 511560, 511560, 797810, 511560, 815413, 797810, 797810, 511560, 45223, 45223, 812630, 915333, 45223, 812630, 915333, 45223, 812630, 815413, 797810, 797810, 952287, 815413, 303683, 154967, 538217, 538217, 628757, 303683, 154967, 154967, 154967, 628757, 915333, 290779, 290779, 45223, 424862, 424862, 183489, 183489, 628757, 673651, 673651, 677394, 698619, 698619, 154967, 154967, 698619, 628757, 628757, 628757, 261698, 403721, 45223, 290779, 290779, 403721, 403721, 403721, 84875, 831664, 698619, 831664, 698619, 698619, 698619, 831664, 831664, 831664, 628757, 698619, 628757, 698619, 332856, 628757, 628757, 332856, 628757, 698619, 628757, 698619, 332856, 332856, 183489, 183489, 890686, 890686, 511560, 424862, 424862, 511560, 600730, 600730, 511560, 511560, 812630, 403721, 92751, 92751, 812630, 812630, 812630, 952287, 952287, 403721, 485421, 485421, 797810, 915333, 915333, 45223, 890686, 261698, 261698, 698619, 183489, 183489, 332856, 332856, 183489, 698619, 183489, 673651, 154967, 673651, 831664, 831664, 673651, 764371, 764371, 511560, 290779, 915333, 511560, 290779, 915333, 511560, 915333, 915333, 698619, 628757, 628757, 628757, 628757, 154967, 890686, 303683, 154967, 890686, 303683, 154967, 838211, 838211, 92751, 92751, 952287, 303683, 538217, 538217, 890686, 890686, 303683, 303683, 890686, 698619, 261698, 890686, 698619, 698619, 628757, 764371, 332856, 628757, 764371, 332856, 628757, 628757, 628757, 764371, 698619, 698619, 828703, 812630, 812630, 812630, 84875, 84875, 677394, 677394, 677394, 600730, 403721, 403721, 424862, 511560, 511560, 600730, 600730, 45223, 828703, 828703, 812630, 393337, 403721, 92751, 92751, 92751, 812630, 393337, 403721, 45223, 45223, 815413, 815413, 154967, 890686, 890686, 154967, 154967, 154967, 154967, 261698, 261698, 952287, 511560, 952287, 511560, 45223, 45223, 45223, 847481, 847481, 288890, 896591, 154967, 896591, 896591, 154967, 952287, 797810, 797810, 183489, 698619, 698619, 183489, 628757, 628757, 303683, 303683, 183489, 332856, 628757, 303683, 332856, 628757, 303683, 698619, 698619, 261698, 288890, 288890, 538217, 538217]\n"
          ]
        }
      ],
      "source": [
        "# Importing pandas library as pd\n",
        "import pandas as pd\n",
        "\n",
        "# Reading data from csv files\n",
        "df1 = pd.read_csv('Tutorial22_df.csv')\n",
        "df2 = pd.read_csv('Tutorial22_xG_df.csv')\n",
        "\n",
        "# Defining global variables\n",
        "global successful_pass, successful_reception, shot_attempt\n",
        "\n",
        "\n",
        "def ShotAssist():\n",
        "    \"\"\"\n",
        "    If a \"Shot Assist\" is defined as a sequence of events with the same possessionid where there is: 1) a\n",
        "    successful pass followed by 2) a successful reception by a teammate and then without giving up the puck 3) the\n",
        "    receiving player has a shot attempt, create a column flagging shots that have a Shot Assist. Which player(s) had\n",
        "    the most assisted shots in the game and how many assisted shots did they have?\n",
        "\n",
        "    \"\"\"\n",
        "    successful_pass, successful_reception, shot_attempt = 0, 0, 0\n",
        "\n",
        "    # Dictionary to store count of Short Assist. Key: PossessionId, Value: number of triplet variables\n",
        "    PID_to_ShortAssistCount = {}\n",
        "\n",
        "    # Sorting the data by possession id in ascending order\n",
        "    Sorted_df1_data = df1.sort_values(by=['possessionid'], ascending=True)\n",
        "\n",
        "    # Assigning temporary Possession Id\n",
        "    tempPid = next(Sorted_df1_data.iterrows())[1][8]\n",
        "\n",
        "    # Iterating through data row-by-row\n",
        "    for index, row in Sorted_df1_data.iterrows():\n",
        "\n",
        "        # Fetching possesion Id\n",
        "        Pid = row['possessionid']\n",
        "\n",
        "        # If possession id same as of previous iteration\n",
        "        if tempPid == Pid:\n",
        "\n",
        "            # Making counts for successful pass, successful reception & attempted shot\n",
        "            if row['outcome'] == 'successful':\n",
        "                if row['eventname'] == 'pass':\n",
        "                    successful_pass += 1\n",
        "                elif row['eventname'] == 'reception':\n",
        "                    successful_reception += 1\n",
        "            if row['eventname'] == 'shot':\n",
        "                shot_attempt += 1\n",
        "\n",
        "        # If possession id has changed compared to previous iteration\n",
        "        else:\n",
        "            # Storing the count of Shot assist in dictionary against the possession id\n",
        "            PID_to_ShortAssistCount[tempPid] = min(successful_pass, successful_reception, shot_attempt)\n",
        "\n",
        "            # Reinitialize the variables value for the next id\n",
        "            successful_pass, successful_reception, shot_attempt = 0, 0, 0\n",
        "\n",
        "            # Updating Possesion Id\n",
        "            Pid = row['possessionid']\n",
        "            tempPid = Pid\n",
        "\n",
        "            # Making counts for successful pass, successful reception & attempted shot\n",
        "            if row['outcome'] == 'successful':\n",
        "                if row['eventname'] == 'pass':\n",
        "                    successful_pass += 1\n",
        "                elif row['eventname'] == 'reception':\n",
        "                    successful_reception += 1\n",
        "            if row['eventname'] == 'shot':\n",
        "                shot_attempt += 1\n",
        "\n",
        "    # Sorting the dictionary in the descending order of Assist Count\n",
        "    PID_to_ShortAssistCount = sorted(PID_to_ShortAssistCount.items(), key=lambda x: x[1], reverse=True)\n",
        "    PID_to_ShortAssistCount = dict(PID_to_ShortAssistCount)\n",
        "\n",
        "    # Storing the number of the highest assist count\n",
        "    higestAssistCount = PID_to_ShortAssistCount[list(PID_to_ShortAssistCount.keys())[0]]\n",
        "\n",
        "    # Array of Possession ids with the highest assist count\n",
        "    maxPID_Array = [i for i in PID_to_ShortAssistCount if PID_to_ShortAssistCount[i] >= higestAssistCount]\n",
        "\n",
        "    # Array to store playerids with max number of assist shots\n",
        "    PlayersList = []\n",
        "\n",
        "    for i in maxPID_Array:\n",
        "        PlayersList.extend(df1[(df1['possessionid'] == i)]['playerid'].tolist())\n",
        "\n",
        "    print('The below list of players ids have the most number of assisted shots with the number being {}'.format(\n",
        "        higestAssistCount))\n",
        "    print(PlayersList)\n",
        "\n",
        "\n",
        "ShotAssist()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "c6779d7f",
      "metadata": {
        "id": "c6779d7f"
      },
      "source": [
        "## Q7)\n",
        "### a) What is highest xg among the goals that were scored and why do you think it was this high? \n",
        "### b) Did this goal have a shot assist?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "00833bad",
      "metadata": {
        "id": "00833bad",
        "outputId": "388723d7-4129-476c-c60a-8f9e396e5ddd"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "The highest xg among the goals that were scored is 0.999534607\n",
            "I believe being outside type player and making a successful shot from the offensive zone could be a deciding factor \n",
            "\n",
            "Comments: This goal doesn't have a Shot Assist primary becuase it is the only record for its possession id = 555, and doesn't have successful pass & successful reception as required\n"
          ]
        }
      ],
      "source": [
        "# Importing pandas library as pd\n",
        "import pandas as pd\n",
        "\n",
        "# Reading data from csv files\n",
        "df1 = pd.read_csv('Tutorial22_df.csv')\n",
        "df2 = pd.read_csv('Tutorial22_xG_df.csv')\n",
        "\n",
        "\n",
        "def higestXG_count():\n",
        "    \"\"\" What is highest xg among the goals that were scored and why do you think it was this high? \"\"\"\n",
        "\n",
        "    # Fetching the compiled game time data from the successful goaled shots\n",
        "    Goal_Data = df1[(df1['goal'] == 1)]['compiledgametime'].tolist()\n",
        "\n",
        "    # Array to store xg values for goaled shots\n",
        "    xg_Array = list()\n",
        "\n",
        "    # Storing xg values in the array\n",
        "    for i in Goal_Data:\n",
        "        xg_Array.append(df2[(df2['compiledgametime'] == i)]['xg'].tolist()[0])\n",
        "\n",
        "    print('The highest xg among the goals that were scored is {}'.format(max(xg_Array)))\n",
        "    print('I believe being outside type player and making a successful shot from the offensive zone could be a '\n",
        "          'deciding factor ')\n",
        "\n",
        "\n",
        "def comments():\n",
        "    \"\"\" Did this goal have a shot assist? \"\"\"\n",
        "\n",
        "    print('\\nComments: This goal doesn''\\'t have a Shot Assist primary becuase it is the only record for its '\n",
        "          'possession id = 555, and doesn''\\'t have successful pass & successful reception as required')\n",
        "\n",
        "\n",
        "higestXG_count()\n",
        "comments()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "78a1e7c5",
      "metadata": {
        "id": "78a1e7c5"
      },
      "source": [
        "## Q8) \n",
        "### a) Consider other shots with high xg values, without engineering any additional features (aside from the columns you've already been asked to create in the questions above), use a statistical technique of your choice to show the highest predictors of a goal within this dataset.\n",
        "### b) Please explain your reasoning for choosing this technique and explain your findings\n",
        "\n",
        "### Hint: look back at the columns you were asked to create, along with the columns already provided in the event dataset, what would lead to dangerous shot attempts?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "41ff1fbd",
      "metadata": {
        "id": "41ff1fbd",
        "outputId": "62531e55-6a1c-4a83-d7eb-eb51a1c86417"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Optimization terminated successfully.\n",
            "         Current function value: 0.357702\n",
            "         Iterations 7\n",
            "                           Logit Regression Results                           \n",
            "==============================================================================\n",
            "Dep. Variable:                     xg   No. Observations:                    2\n",
            "Model:                          Logit   Df Residuals:                        1\n",
            "Method:                           MLE   Df Model:                            0\n",
            "Date:                Sun, 12 Mar 2023   Pseudo R-squ.:                     inf\n",
            "Time:                        03:43:26   Log-Likelihood:               -0.71540\n",
            "converged:                       True   LL-Null:                        0.0000\n",
            "Covariance Type:            nonrobust   LLR p-value:                       nan\n",
            "==============================================================================\n",
            "                 coef    std err          z      P>|z|      [0.025      0.975]\n",
            "------------------------------------------------------------------------------\n",
            "distance       0.0852      0.134      0.638      0.523      -0.177       0.347\n",
            "==============================================================================\n",
            "\n",
            "\n",
            "Model: Used Logit Regression to show highest predictor of goal value which is the distance\n",
            "Reason: coefficients, standard errors, p-values, confidence intervals of dependent variable show the direction and intensity of the link between each predictor variable and the independent variable.\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "C:\\Users\\kunaa\\Documents\\Kunaal Gupta\\SportLogic Interview\\venv\\lib\\site-packages\\statsmodels\\base\\model.py:592: HessianInversionWarning: Inverting hessian failed, no bse or cov_params available\n",
            "  warnings.warn('Inverting hessian failed, no bse or cov_params '\n",
            "C:\\Users\\kunaa\\Documents\\Kunaal Gupta\\SportLogic Interview\\venv\\lib\\site-packages\\statsmodels\\base\\model.py:592: HessianInversionWarning: Inverting hessian failed, no bse or cov_params available\n",
            "  warnings.warn('Inverting hessian failed, no bse or cov_params '\n",
            "C:\\Users\\kunaa\\Documents\\Kunaal Gupta\\SportLogic Interview\\venv\\lib\\site-packages\\statsmodels\\discrete\\discrete_model.py:3511: RuntimeWarning: divide by zero encountered in scalar divide\n",
            "  return 1 - self.llf/self.llnull\n"
          ]
        }
      ],
      "source": [
        "# Importing libraries\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import statsmodels.api as sm\n",
        "\n",
        "# Reading the data from files\n",
        "df1 = pd.read_csv('Tutorial22_df.csv')\n",
        "df2 = pd.read_csv('Tutorial22_xG_df.csv')\n",
        "\n",
        "\n",
        "def addingDistanceCol():\n",
        "    # Fetching the x & y cordinates from dataframe df1\n",
        "    x = np.array(df1[['xcoord']])\n",
        "    y = np.array(df1[['ycoord']])\n",
        "\n",
        "    # Adding a new column called distance which stores distance between centre and specified coordinates\n",
        "    df1['distance'] = ((89 - x) ** 2 + y ** 2) ** 0.5  # pythagoras theorem to calc distance\n",
        "\n",
        "\n",
        "def StatModel():\n",
        "    addingDistanceCol()\n",
        "\n",
        "    # Merging both the dataframes based on compiled game time\n",
        "    df = pd.merge(df1, df2, on=[\"compiledgametime\", 'playerid', 'teamid'])\n",
        "\n",
        "    xg_shots = df[df['xg'] > 0.5]\n",
        "\n",
        "    # Dependent variable and independent variables\n",
        "    Y = xg_shots['xg']\n",
        "    X = xg_shots[['distance']]\n",
        "\n",
        "    # Defining the model\n",
        "    model = sm.Logit(Y, X).fit()\n",
        "    print(model.summary())\n",
        "\n",
        "    print('\\n\\nModel: Used Logit Regression to show highest predictor of goal value which is the distance')\n",
        "    print('Reason: coefficients, standard errors, p-values, confidence intervals of dependent variable show the '\n",
        "          'direction and intensity of the link between each predictor variable and the independent variable.')\n",
        "\n",
        "\n",
        "StatModel()\n"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.9"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}