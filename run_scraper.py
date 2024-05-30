from src.scraper import scrape_profiles

if __name__ == "__main__":
    # Example list of LinkedIn profile URLs
    profile_urls = [
        "https://www.linkedin.com/in/some-profile",
        # Add more URLs as needed
    ]
    scrape_profiles(profile_urls)
