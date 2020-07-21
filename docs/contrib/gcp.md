>You don't need your own gcp project to test this, since pushing to a branch will run tests for you, but this will make your feedback loop way much faster.

To get everything set up you should have a gcp project, if you have a gmail account and didn't use your trial, you can get free quota for 300$ which is sufficient for all testing we're doing in `storage-bucket`.

Get the gcloud cli - [quickstart](https://cloud.google.com/sdk/docs/quickstarts)

Make a service account or [find the default SA for storage bucket](https://cloud.google.com/storage/docs/getting-service-account)

Change directory to this project directory and create a key with:
```
gcloud iam service-accounts keys create key.json --iam-account serviceaccount-name@project-id.iam.gserviceaccount.com
```
replace `serviceaccount-name` and `project-id` with your own values.

This will create the file `key.json` in your working dir.

NOTE: If you decide to name file differently make sure you added its name into `.gitignore`, so it won't get pushed into the repo.

And thats all you need to get up and running and start developing.
