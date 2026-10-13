import requests
from typing import Optional
import sys


def _fetch_live_cube_meta() -> Optional[str]:
        base_url = "http://localhost:4000/cubejs-api/v1"
        # token = "# Add API token here"
        try:
            response = requests.get(f"{base_url}/meta", headers={"Authorization": token})
            response.raise_for_status()
            cubes = response.json().get("cubes", [])
            
            schema_summary = []
            for cube in cubes:
                cube_name = cube.get("name")
                measures = [m.get("name") for m in cube.get("measures", [])]
                dimensions = [d.get("name") for d in cube.get("dimensions", [])]
                
                schema_summary.append(f"Cube: {cube_name}")
                schema_summary.append(f"  - Available Measures: {measures}")
                schema_summary.append(f"  - Available Dimensions: {dimensions}\n")

            # print(schema_summary)    
            return "\n".join(schema_summary)
        except Exception as e:
            print(f"Warning: Failed to fetch live schema metadata: {e}", file=sys.stderr)
            return None


if __name__ == "__main__":
     schema_result = _fetch_live_cube_meta()
     print(schema_result)