# ZenoTime

ZenoTime is a powerful and user-friendly command-line tool for viewing and managing world time zones. It provides current time information for major cities worldwide and allows searching through all available time zones.

## Features

- Display current time for major cities across different regions
- Search for specific time zones
- View time in any supported time zone
- List all available time zones
- Grouped display by geographical regions
- Clean, formatted output with UTC offsets

## Installation

1. Ensure you have Python 3.6+ installed
2. Install the required dependencies:
```bash
pip install pytz
```

## Usage

```bash
python zenotime.py [options]
```

### Options

- `-t, --timezone TIMEZONE`: Show time for a specific timezone
- `-s, --search QUERY`: Search for timezones containing the query
- `-l, --list`: List all available timezones
- Running without options shows time in major cities worldwide

### Examples

```bash
# Show time in major cities
python zenotime.py

# Search for timezones containing 'tokyo'
python zenotime.py -s tokyo

# Show time in Tokyo
python zenotime.py -t Asia/Tokyo

# List all available timezones
python zenotime.py -l
```

## Output Format

Times are displayed in the following format:
```
Timezone                              | YYYY-MM-DD HH:MM:SS Zone (UTC±HHMM)
```

Example:
```
Asia/Tokyo                            | 2025-01-20 23:30:45 JST (UTC+0900)
```

## Supported Regions

- North America
- South America
- Europe
- Asia
- Oceania
- Africa

## Major Cities Coverage

ZenoTime includes time information for major cities including:

- Americas: New York, Los Angeles, Chicago, Toronto, São Paulo, Buenos Aires
- Europe: London, Paris, Berlin, Moscow, Istanbul
- Asia: Tokyo, Shanghai, Singapore, Dubai, Hong Kong
- Oceania: Sydney, Melbourne, Auckland
- Africa: Cairo, Lagos, Johannesburg

## Dependencies

- Python 3.6+
- pytz

## Error Handling

- Displays appropriate error messages for invalid time zones
- Graceful exit with Ctrl+C
- Clear feedback for timezone searches with no results

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is open source and available under the MIT License.
