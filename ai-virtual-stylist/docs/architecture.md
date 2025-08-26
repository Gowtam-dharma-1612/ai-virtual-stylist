# Architecture Notes

- **Input:** user image (upload or path)
- **Processing:** image pre-processing → attribute detection (stubs) → feature vector
- **Recommendation:** rules/ML to map features to outfits
- **Output:** list of outfit suggestions + confidence

Data structures:
- Lists/Arrays — feature vectors
- Dicts/HashMaps — outfit attributes and config
- Queue — processing pipeline (if asynchronous worker is used)
