#!/bin/bash

# Export environment variables
export DB_NAME="trading_data.db"
export CSV_FILE="trading_data.csv"
export NUM_RECORDS=100

# Function to create the TradingData table
create_table() {
    sqlite3 $DB_NAME <<EOF
CREATE TABLE IF NOT EXISTS TradingData (
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    date TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER
);
EOF
}

# Function to insert a new trading record into the TradingData table
insert_trading_data() {
    local id=$1
    local symbol=$2
    local date=$3
    local open=$4
    local high=$5
    local low=$6
    local close=$7
    local volume=$8
    sqlite3 $DB_NAME <<EOF
INSERT INTO TradingData (id, symbol, date, open, high, low, close, volume) VALUES ($id, '$symbol', '$date', $open, $high, $low, $close, $volume);
EOF
}

# Function to generate random trading data and insert into TradingData table
generate_random_data() {
    for i in $(seq 1 $NUM_RECORDS); do
        symbol="SYM$((RANDOM % 100))"
        date=$(date -v -"$((RANDOM % 365))"d +%Y-%m-%d)
        open=$(awk -v min=100 -v max=500 'BEGIN{srand(); print min+rand()*(max-min)}')
        high=$(awk -v min=$open -v max=600 'BEGIN{srand(); print min+rand()*(max-min)}')
        low=$(awk -v min=50 -v max=$open 'BEGIN{srand(); print min+rand()*(max-min)}')
        close=$(awk -v min=$low -v max=$high 'BEGIN{srand(); print min+rand()*(max-min)}')
        volume=$((RANDOM % 10000 + 1000))
        insert_trading_data $i "$symbol" "$date" $open $high $low $close $volume
    done
}

# Function to query the database and save the results to a CSV file
query_database() {
    sqlite3 -header -csv $DB_NAME "SELECT * FROM TradingData;" > $CSV_FILE
}

# Main script execution
create_table
generate_random_data
query_database

echo "Database setup complete. Data saved to $CSV_FILE."