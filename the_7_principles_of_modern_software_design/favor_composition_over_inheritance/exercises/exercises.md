Consider the following code:

```python
class ACCloud(CloudProvider):
  def __init__(self, bucket_name: str, region: str) -> None:
    authentication = GoogleAuth("service_key.json")
    super().__init__(
      region=region,
      http_auth=authentication,
      secure=True,
    )
    self.bucket_name = bucket_name

  def find_files(
    self,
    query: str,
    max_result: int
  ) -> list[str]:
    response = self.filter_by_query(
      bucket=self.bucket_name,
      query=query,
      max=max_result
    )
    return response["result"]["data"][0]

class VideoStorage(ACCloud):
  def __init__(self) -> None:
    super().__init__(
      bucket_name="video-backup.arjancodes.com",
      region="eu-west-1c",
    )
```

The code extends the capability of `CloudProvider` by using two inheritance layers: one layer to add a convenience method for finding files, and one layer to create a default video storage access point for `ACCloud`.

a) Refactor this code so that it no longer uses inheritance, but relies on composition instead.

b) Refactor the code once more so that `find_files` is no longer dependent on the `cloudengine` package.
