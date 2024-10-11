# Device MQTT communications

## General structer

```

{
  id: uuid || null,
  request: "UPDATE_DATABESE" || "REQUEST_DATABASE" || "LOG",
  data: any,
  error: string
}

```

## Data example

**Database brodcast update**

```
{
  id: null,
  request: "UPDATE_DATABESE",
  data: [
    {
    id: string,
    status: boolen,
    }
  ],
}
```

**Database request**
on reboot device or no database exist or empty, if database exist `cheaksum` will be sent else data null

```
{
  id: uuid,
  request: "REQUEST_DATABASE",
  data: string || null,
}
```

**Logs**
will be ganerated in device and sent to server as list, if no internet log will be stored

```
{
  id: uuid,
  request: "LOG",
  data: string[],
}
```
