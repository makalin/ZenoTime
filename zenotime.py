from datetime import datetime
import pytz
import argparse
import sys
from typing import Optional, List
import textwrap

class ZenoTime:
    def __init__(self):
        self.all_timezones = sorted(pytz.all_timezones)
        
    def get_current_time(self, timezone: str) -> Optional[datetime]:
        """Get current time for a specific timezone."""
        try:
            tz = pytz.timezone(timezone)
            return datetime.now(tz)
        except pytz.exceptions.UnknownTimeZoneError:
            return None

    def search_timezone(self, query: str) -> List[str]:
        """Search for timezones matching the query."""
        query = query.lower()
        return [tz for tz in self.all_timezones if query in tz.lower()]

    def format_time(self, dt: datetime) -> str:
        """Format datetime object into a readable string."""
        return dt.strftime("%Y-%m-%d %H:%M:%S %Z (UTC%z)")

    def display_time(self, timezone: str) -> None:
        """Display time for a specific timezone."""
        time = self.get_current_time(timezone)
        if time:
            print(f"{timezone:35} | {self.format_time(time)}")
        else:
            print(f"Error: Invalid timezone '{timezone}'")

    def list_all_times(self) -> None:
        """Display current time for all major cities."""
        major_timezones = [
            # North America
            "America/New_York",      # New York, USA
            "America/Los_Angeles",   # Los Angeles, USA
            "America/Chicago",       # Chicago, USA
            "America/Toronto",       # Toronto, Canada
            "America/Vancouver",     # Vancouver, Canada
            "America/Mexico_City",   # Mexico City, Mexico
            "America/Panama",        # Panama City, Panama
            "America/Havana",        # Havana, Cuba
            
            # South America
            "America/Sao_Paulo",     # São Paulo, Brazil
            "America/Buenos_Aires",  # Buenos Aires, Argentina
            "America/Santiago",      # Santiago, Chile
            "America/Lima",          # Lima, Peru
            "America/Bogota",        # Bogota, Colombia
            
            # Europe
            "Europe/London",         # London, UK
            "Europe/Paris",          # Paris, France
            "Europe/Berlin",         # Berlin, Germany
            "Europe/Rome",           # Rome, Italy
            "Europe/Madrid",         # Madrid, Spain
            "Europe/Amsterdam",      # Amsterdam, Netherlands
            "Europe/Moscow",         # Moscow, Russia
            "Europe/Istanbul",       # Istanbul, Turkey
            "Europe/Stockholm",      # Stockholm, Sweden
            "Europe/Oslo",           # Oslo, Norway
            "Europe/Copenhagen",     # Copenhagen, Denmark
            "Europe/Vienna",         # Vienna, Austria
            "Europe/Warsaw",         # Warsaw, Poland
            
            # Asia
            "Asia/Tokyo",           # Tokyo, Japan
            "Asia/Shanghai",        # Shanghai, China
            "Asia/Singapore",       # Singapore
            "Asia/Dubai",           # Dubai, UAE
            "Asia/Hong_Kong",       # Hong Kong
            "Asia/Seoul",           # Seoul, South Korea
            "Asia/Bangkok",         # Bangkok, Thailand
            "Asia/Taipei",          # Taipei, Taiwan
            "Asia/Manila",          # Manila, Philippines
            "Asia/Jakarta",         # Jakarta, Indonesia
            "Asia/Mumbai",          # Mumbai, India
            "Asia/Kolkata",         # Kolkata, India
            "Asia/Tel_Aviv",        # Tel Aviv, Israel
            "Asia/Ho_Chi_Minh",     # Ho Chi Minh City, Vietnam
            
            # Oceania
            "Australia/Sydney",      # Sydney, Australia
            "Australia/Melbourne",   # Melbourne, Australia
            "Australia/Brisbane",    # Brisbane, Australia
            "Australia/Perth",       # Perth, Australia
            "Pacific/Auckland",      # Auckland, New Zealand
            "Pacific/Fiji",         # Fiji
            "Pacific/Honolulu",     # Honolulu, Hawaii
            
            # Africa
            "Africa/Cairo",         # Cairo, Egypt
            "Africa/Lagos",         # Lagos, Nigeria
            "Africa/Johannesburg",  # Johannesburg, South Africa
            "Africa/Nairobi",       # Nairobi, Kenya
            "Africa/Casablanca",    # Casablanca, Morocco
            "Africa/Addis_Ababa",   # Addis Ababa, Ethiopia
            "Africa/Dar_es_Salaam", # Dar es Salaam, Tanzania
            
            # Central Asia
            "Asia/Tashkent",        # Tashkent, Uzbekistan
            "Asia/Almaty",          # Almaty, Kazakhstan
            "Asia/Dhaka",           # Dhaka, Bangladesh
            "Asia/Karachi",         # Karachi, Pakistan
            
            # South Pacific
            "Pacific/Port_Moresby", # Port Moresby, Papua New Guinea
            "Pacific/Guadalcanal",  # Honiara, Solomon Islands
            "Pacific/Noumea"        # Noumea, New Caledonia
        ]
        
        print("\nWorld Time Overview:")
        print("-" * 80)
        
        # Group timezones by region for better readability
        regions = {
            "North America": [],
            "South America": [],
            "Europe": [],
            "Asia": [],
            "Oceania": [],
            "Africa": [],
        }
        
        for tz in major_timezones:
            region = next(r for r in regions.keys() if r.split()[0] in tz)
            regions[region].append(tz)
        
        for region, timezones in regions.items():
            if timezones:
                print(f"\n{region}:")
                print("-" * 40)
                for tz in sorted(timezones):
                    self.display_time(tz)

def main():
    parser = argparse.ArgumentParser(
        description="ZenoTime - Worldwide Time Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
            Examples:
              zenotime                    # Show time in major cities
              zenotime -s tokyo           # Search for timezones containing 'tokyo'
              zenotime -t Asia/Tokyo      # Show time in Tokyo
              zenotime -l                 # List all available timezones
        """)
    )
    parser.add_argument('-t', '--timezone', help='Show time for specific timezone')
    parser.add_argument('-s', '--search', help='Search for timezone')
    parser.add_argument('-l', '--list', action='store_true', help='List all available timezones')

    args = parser.parse_args()
    zeno = ZenoTime()

    if args.timezone:
        zeno.display_time(args.timezone)
    elif args.search:
        matches = zeno.search_timezone(args.search)
        if matches:
            print("\nMatching timezones:")
            print("-" * 80)
            for tz in matches:
                zeno.display_time(tz)
        else:
            print(f"No timezones found matching '{args.search}'")
    elif args.list:
        print("\nAvailable timezones:")
        print("-" * 80)
        for tz in zeno.all_timezones:
            print(tz)
    else:
        zeno.list_all_times()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting ZenoTime...")
        sys.exit(0)
