# cc_test_module
A concourse cicd pipline test module

## Pipeline
- trigger on lib repo
- trigger on cli repo
- run uts on both
- if pass uts, commit to unit-test-pass branch
- report to slack uts result
- run its on both
- if pass its, commit to int-tests-pass branch
- report to slack its result
- run sts on both
- if pass sts, commit to sys-tests-pass branch
