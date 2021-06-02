### 介绍 Introduction

将[动漫花园](http://dmhy.org)首页条目和搜索结果转换成 JSON 格式供其他服务使用。
Convert homepage and search results of [dmhy.org](http://dmhy.org) to JSON format for further use of other service.

### 安装及部署 Installation & Deployment

#### 通过 docker 部署 Deploy in Docker
```shell
$ git clone zxf1023818103/dmhy-api
$ docker build --tag dmhy-api dmhy-api
$ docker tag dmhy-api:latest dmhy-api:v1.0.0
$ docker run --publish 5000:5000 dmhy-api
$ curl http://localhost:5000/api/page/1
[{
  "title": ...,
  "post_datetime": ...,
  ...
},{
  ...
}, ...]
```

#### 直接运行 Run anyway
```shell
$ git clone zxf1023818103/dmhy-api && cd dmhy-api
$ pip3 install -r requirements.txt
$ python -m flask run --host=0.0.0.0
$ curl http://localhost:5000/api/page/1
[{
  "title": ...,
  "post_datetime": ...,
  ...
},{
  ...
}, ...]
```

### 使用 Usage
#### 获取主页或搜索条目 Get homepage or search items

`GET /api/page/:page`

| 参数 Parameter | 类型 Type | 描述 Description | 备注 Note | 是否必须 Required |
|---|----|---|---|----|
| page | 整数 integer | 第几页 Page number | | ✅ |
| keyword | 字符串 string | 搜索关键词 Keyword | |
| simplified_chinese | 布尔值 boolean | 是否进行简繁转换 Translate to Simplified Chinese | `true`/`false` | |

结果以 JSON 数组形式返回。

Return result with JSON array.

| 参数 Parameter | 类型 Type | 描述 Description | 备注 Note |
|---------------|-----------|-----------------|----------|
| post_datetime | 字符串 string | 发布时间 Post Datetime | |
| team_name | 字符串 string | 字幕组名称 Team Name |
| team_id | 字符串 string | 字幕组 ID Team ID | |
| title | 字符串 string | 标题 Title |  |
| sort_name | 字符串 string | 资源分类名称 Resource Class Name | |
| sort_id | 字符串 string | 资源分类 ID Resource Class ID | |
| magnet | 字符串 string | 磁力链接 Magnet Link |  |
| size | 字符串 string | 资源大小 Resource Size |  |
| downloading_number | 字符串 string | 正在下载的人数 Peoples Downloading Files | |
| seeding_number | 字符串 string | 正在做种的人数 Peoples Seeding Files | |
| finished_number | 字符串 string | 完成下载的人数 Peoples Completed File Download | |