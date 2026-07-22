<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can mount an Open Container Initiative (OCI)-compliant container image directly into a pod, making the files within the image accessible to the containers without the need to include them in the base image, which allows you to host the data in OCI-compliant registries.

# Understanding image volumes

You can use an *image volume* to mount an Open Container Initiative (OCI)-compliant container image directly into a pod, making the files within the image accessible to the containers without the need to include them in the base image. This means you can host the data in an OCI-compliant registry.

By using an image volume in a pod, you can take advantage of the OCI image and distribution specification standards to accomplish several tasks including the following use cases:

- You can share configuration files among multiple containers in a pod without needing to include the file in the base image, which minimizes security risks and image size.

- In an artificial intelligence environment, you can use image volumes to mount large language model weights or machine learning model weights in a pod alongside a model-server. You can efficiently serve model weights this way without including them in the model-server container image. Therefore, you can separate the model specifications and content from the executables that process them.

- You can use a public image for a malware scanner and mount it in a volume of private malware signatures, so that you can load those signatures without incorporating the image into a base image, which might not be allowed by the copyright on the public image.

To mount an image volume, include a path to the image in your pod spec with an optional pull policy as described in *Adding an image volume to a pod*.

# Adding an image volume to a pod

To mount an Open Container Initiative (OCI)-compliant container image, use the `volume` parameter to include a path to the image in your pod spec with an optional pull policy. You can create the pod directly or use a controlling object, such as a deployment or replica set.

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file similar to the following.

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: image-volume
    spec:
      containers:
      - name: shell
        command: ["sleep", "infinity"]
        image: debian
        volumeMounts:
        - name: volume
          mountPath: /volume
      volumes:
      - name: volume
        image:
          reference: quay.io/crio/image:v2
          pullPolicy: Always
    ```

    - Specifies an OCI container image that is available on the host machine.

    - Specifies the path to the image.

    - Specifies a pull policy, one of the following options:

      - If `Always`, the kubelet always attempts to pull the image. If the pull fails, the kubelet sets the pod to `Failed`.

      - If `Never`, the kubelet never pulls the image and only uses a local image. The pod becomes `Failed` if any layers of the image are not present locally, or if the manifest for that image is not already cached.

      - If `IfNotPresent` the kubelet pulls the image if it is not present. The pod becomes `Failed` if the image is not present and the pull fails. This is the default.

2.  Create the pod by running the following command:

    ``` terminal
    $ oc create -f <file_name>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Examine the pod to view detailed information about the image pull and mount by using a command similar to the following:

  ``` terminal
  $ oc describe pod <pod_name>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  Name:             image-volume
  Namespace:        default
  # ...
  Volumes:
    volume:
      Type:        Image
      Reference:   quay.io/crio/image:v2
      PullPolicy:  IfNotPresent
  # ...
  Events:
    Type    Reason          Age                From               Message
    ----    ------          ----               ----               -------
  # ...
    Normal  Pulling         46s                kubelet            Pulling image "quay.io/crio/image:v2"
    Normal  Pulled          44s                kubelet            Successfully pulled image "quay.io/crio/image:v2" in 2.261s (2.261s including waiting). Image size: 6707 bytes.
  # ...
  ```

  </div>

  - Indicates that the image was mounted to the pod.

  - Indicates that the image was successfully pulled.

</div>
