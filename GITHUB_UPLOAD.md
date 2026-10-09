# GitHub Upload Steps (Mac)

1. Create a new repository on GitHub, for example:
   `petrol-fuel-demand-prediction`

2. Open Terminal and move into this project folder.

3. Run:
```bash
git init
git add .
git commit -m "Initial fuel demand prediction project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

4. Before pushing real station data, remove private information such as customer names, phone numbers, payment details, vehicle numbers or confidential business records.

5. In the repository README, explain that the included dataset is synthetic if you have not yet replaced it with a real public/anonymized dataset.
