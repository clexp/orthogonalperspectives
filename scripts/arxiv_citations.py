#!/usr/bin/env python3
"""
Fetch most cited papers from arXiv for each year 2000-2010
"""

import requests
import json
import time
from datetime import datetime
from pathlib import Path

def fetch_arxiv_papers(year, max_results=10):
    """Fetch papers from arXiv for a specific year"""
    
    # arXiv API endpoint
    base_url = "http://export.arxiv.org/api/query"
    
    # Search parameters
    params = {
        'search_query': f'cat:cs.AI+OR+cat:cs.LG+OR+cat:stat.ML+AND+submittedDate:[{year}0101+TO+{year}1231]',
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        # Parse XML response (simplified)
        # Note: This is a basic implementation. For production, use proper XML parsing
        content = response.text
        
        # Extract paper information (simplified parsing)
        papers = []
        lines = content.split('\n')
        
        current_paper = {}
        for line in lines:
            line = line.strip()
            if '<entry>' in line:
                current_paper = {}
            elif '<title>' in line and '</title>' in line:
                title = line.replace('<title>', '').replace('</title>', '').strip()
                current_paper['title'] = title
            elif '<id>' in line and '</id>' in line:
                paper_id = line.replace('<id>', '').replace('</id>', '').strip()
                current_paper['id'] = paper_id
            elif '<summary>' in line and '</summary>' in line:
                summary = line.replace('<summary>', '').replace('</summary>', '').strip()
                current_paper['summary'] = summary
            elif '<published>' in line and '</published>' in line:
                published = line.replace('<published>', '').replace('</published>', '').strip()
                current_paper['published'] = published
            elif '</entry>' in line and current_paper:
                papers.append(current_paper.copy())
        
        return papers
        
    except Exception as e:
        print(f"Error fetching papers for {year}: {e}")
        return []

def get_citation_data(paper_id):
    """Get citation data for a paper (placeholder - would need external API)"""
    # This would require integration with citation databases like:
    # - Google Scholar API
    # - Semantic Scholar API
    # - Microsoft Academic Graph
    # - Scopus API
    
    # For now, return placeholder data
    return {
        'citations': 0,
        'sources': []
    }

def main():
    """Main function to fetch papers for each year"""
    
    output_dir = Path('export_arxiv_papers')
    output_dir.mkdir(exist_ok=True)
    
    all_papers = {}
    
    # Fetch papers for each year 2000-2010
    for year in range(2000, 2011):
        print(f"Fetching papers for {year}...")
        
        papers = fetch_arxiv_papers(year, max_results=20)
        
        # Add citation data (placeholder)
        for paper in papers:
            paper['citation_data'] = get_citation_data(paper.get('id', ''))
        
        all_papers[year] = papers
        
        # Save individual year data
        year_file = output_dir / f'papers_{year}.json'
        with open(year_file, 'w', encoding='utf-8') as f:
            json.dump(papers, f, indent=2, ensure_ascii=False)
        
        print(f"  Saved {len(papers)} papers for {year}")
        
        # Be nice to the API
        time.sleep(1)
    
    # Save combined data
    combined_file = output_dir / 'all_papers.json'
    with open(combined_file, 'w', encoding='utf-8') as f:
        json.dump(all_papers, f, indent=2, ensure_ascii=False)
    
    print(f"\nExport complete! Papers saved to {output_dir}/")
    print(f"Combined file: {combined_file}")
    
    # Print summary
    for year, papers in all_papers.items():
        print(f"{year}: {len(papers)} papers")

if __name__ == "__main__":
    main() 