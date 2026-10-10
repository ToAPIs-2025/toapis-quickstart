# GPT Image 2 Prompts — ToAPIs

14 adapted prompt recipes for product photography, cinematic scenes, food, architecture, illustration, portraits, macro photography and concept art.

**Preparation status:** the prompts and request settings are ready. ToAPIs outputs have not been generated yet; this is a preparation branch, not the completed gallery release.

[Get an API key](https://toapis.com/dashboard/tokens?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_top_key) · [Current pricing](https://toapis.com/en/pricing?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_top_pricing) · [Quickstart](https://github.com/ToAPIs-2025/toapis-quickstart)

## Generation settings

Every recipe uses `gpt-image-2`, `resolution: "1k"`, `n: 1` and URL output. The source recipe aspect ratio is preserved. No VIP model, resolution upgrade, or source image is used.

1K is the API resolution tier, not a promise that every image's longest edge is 1024 pixels. The documented 1K sizes include 1024×1024 for 1:1, 1536×864 for 16:9, 1024×768 for 4:3, 768×1024 for 3:4, and 1536×1024 for 3:2. Generated dimensions must be checked against these settings.

[GPT Image 2 API reference](https://docs.toapis.com/docs/en/api-reference/images/gpt-image-2/generation)

## Recipes

| Recipe | Category | Aspect ratio | Resolution | Output status |
| --- | --- | --- | --- | --- |
| Product Hero Perfume | Product / e-commerce | 1:1 | 1K | Awaiting generation |
| Cinematic Street Rain | Cinematic still | 16:9 | 1K | Awaiting generation |
| Food Overhead Ramen | Food photography | 4:3 | 1K | Awaiting generation |
| Architectural Dusk | Architecture | 16:9 | 1K | Awaiting generation |
| Illustration Layered Paper | Illustration | 1:1 | 1K | Awaiting generation |
| Fashion Editorial Studio | Fashion portrait | 3:4 | 1K | Awaiting generation |
| Macro Botanical Detail | Macro nature | 3:2 | 1K | Awaiting generation |
| Infographic Dashboard | Design / UI | 16:9 | 1K | Awaiting generation |
| Product Cosmetics Duo | Product | 1:1 | 1K | Awaiting generation |
| Cyberpunk Motorbike | Cinematic | 16:9 | 1K | Awaiting generation |
| Mythic Creature Concept | Concept art | 3:2 | 1K | Awaiting generation |
| Retro Poster Travel | Poster / graphic | 3:4 | 1K | Awaiting generation |
| Gourmet Dessert | Food | 4:3 | 1K | Awaiting generation |
| Fantasy City Aerial | Environment | 16:9 | 1K | Awaiting generation |

Copy the full prompts from [PROMPTS.md](PROMPTS.md); machine-readable requests and source references are in [data/recipes.json](data/recipes.json).

## Generate a recipe

The gallery runner reuses the Quickstart request and task-polling functions, overrides the image ratio for each recipe, and fixes the model and resolution.

```bash
python examples/generate_gallery.py --dry-run
python examples/generate_gallery.py --id 01-product-hero-perfume --env-file /path/to/private.env
```

Without `--id`, a live run processes all 14 recipes sequentially. A generation makes a paid API request according to your account's current pricing. Completed records are skipped on subsequent runs. Previously submitted tasks are resumed rather than resubmitted.

Keep the environment file outside the repository. It should provide `TOAPIS_API_KEY` and optionally `TOAPIS_BASE_URL`. The runner never prints the key. The default API base follows the existing Quickstart; use your established base URL when generating.

## Outputs and measurements

Outputs will be saved in `assets/`, with sanitized task records in `data/runs/`. No competitor image or competitor price is presented as a ToAPIs result. Unavailable cost fields remain null. Verify charges using your account's Usage Logs before publishing numerical cost claims.

## Sources and adaptation

These recipes adapt the MIT-licensed prompt text from the Nano Banana Pro and Grok Imagine reference repositories supplied for this project. The original subject, composition and aspect ratio are retained; lighting, palette, material details and constraints have been adjusted. All published gallery images must be newly generated through ToAPIs.

Full attribution and the upstream license notice are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The upstream prompts were written for other models; their behavior on GPT Image 2 has not yet been assessed.

## About ToAPIs

Maintained by ToAPIs to demonstrate its image API. ToAPIs is a third-party API service; model names belong to their respective owners.

[Generate through ToAPIs](https://toapis.com/dashboard/tokens?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_bottom_key)
