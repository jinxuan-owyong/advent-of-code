#!/usr/bin/sh
set -e
if [ -z "$2" ]
then
    year=$(date '+%Y')
else
    year="$2"
fi
if [ -z "$1" ]
then
    day=$(TZ=':US/Eastern' date '+%-d')
else
    day="$1"
fi

session_path="$(dirname $0)/session"
session=$(cat "$session_path")
year_path=$(dirname $0)/$year
day_path=$year_path/$(printf %02d $day)

mkdir -p $day_path/1
mkdir -p $day_path/2
set -x
curl -H "Cookie: session=$session" "https://adventofcode.com/${year}/day/${day}/input" > $day_path/1/puzzle.in
touch $day_path/1/1.in
cp 2024/template.go $day_path/1/part1.go
touch $day_path/2/part2.go

ln -s ../1/1.in $day_path/2/1.in
ln -s ../1/puzzle.in $day_path/2/puzzle.in

echo "| $day |   |   |   |" >> $year_path/README.md
