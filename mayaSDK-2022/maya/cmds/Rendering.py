
from typing import Any, Container, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar, Union, Text



def assignViewportFactories(materialFactory: str = "",nodeType: str = "",textureFactory: str = "") -> None:
    """
    ディスプレイ用のビューポート ファクトリをマテリアルまたはテクスチャとして設定します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    materialFactory (string): ノードタイプにmaterialFactoryを設定または照会します。

    -----------------------------------------

    nodeType (string): ノードタイプ。

    -----------------------------------------

    textureFactory (string): ノードタイプにtextureFactoryを設定または照会します。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def batchRender(filename: str = "",melCommand: str = "",numProcs: int = 1,preRenderCommand: str = "",remoteRenderMachine: str = "",renderCommandOptions: str = "",showImage: bool = False,status: str = "",useRemoteRender: bool = False,useStandalone: bool = False,verbosity: int = 1) -> None:
    """
    batchRender コマンドは、現在の Maya ファイルの別のレンダリング セッションを作成するために使用します。指定した Maya ファイルがないときは、現在のジョブを終了するかどうか尋ねられます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    filename (string): レンダーするファイル名。空の場合は、テンポラリファイル名が作成されます。

    -----------------------------------------

    melCommand (string): ソフトウェアレンダラ以外のレンダラを実行するために実行するMELコマンド。

    -----------------------------------------

    numProcs (int): 使用するプロセッサの数。0は使用可能なすべてのプロセッサを使用することを意味します。

    -----------------------------------------

    preRenderCommand (string): バッチレンダーを起動する前に実行するコマンド。

    -----------------------------------------

    remoteRenderMachine (string): リモートのレンダーマシンの名前です。Windowsでは使用できません。

    -----------------------------------------

    renderCommandOptions (string): バッチレンダリング用のレンダーコマンドの引数。

    -----------------------------------------

    showImage (boolean): 現在のレンダリングジョブの進行状況を表示します。

    -----------------------------------------

    status (string): バッチレンダリングのステータスを表示するステータス文字列です。

    -----------------------------------------

    useRemoteRender (boolean): リモートレンダリングするか否か。Windowsでは使用できません。

    -----------------------------------------

    useStandalone (boolean): バッチレンダリングを実行するには、シーンを書き出し、スタンドアロン型レンダラを使用してレンダリングします。

    -----------------------------------------

    verbosity (int): バッチレンダリングのステータスを報告する冗長レベルを定義します。1:開始メッセージを1回表示し、すべてのフレームをレンダーする場合にメッセージを1回表示します。2:開始フレームメッセージと終了フレームメッセージだけを表示します。3:すべてのメッセージを表示します(既定)。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def binMembership(addToBin: str = "",exists: str = "",inheritBinsFromNodes: str = "",isValidBinName: str = "",listBins: bool = False,makeExclusive: str = "",notifyChanged: bool = False,removeFromBin: str = "") -> None:
    """
    ノードをビンに割り当てるコマンドです。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    addToBin (string): ノードリスト内のノードをビンに追加します。

    -----------------------------------------

    exists (string): ノードがビンに存在するかどうかを照会します。existsフラグは1つのノードしか指定できません。

    -----------------------------------------

    inheritBinsFromNodes (name): 指定したノードリスト内のノードからフラグの引数にあるノードにビンを継承させます。ノードリストはコマンドのオブジェクトとして指定します。

    -----------------------------------------

    isValidBinName (string): 指定したビン名が有効かどうかを照会します。有効な場合、trueを返します。無効な場合、falseを返します。

    -----------------------------------------

    listBins (boolean): ノードのリストが属するビンのリストを照会して返します。ビンがセレクションリスト内のノードのいずれかを含む場合、返されるビンリストに入ります。

    -----------------------------------------

    makeExclusive (string): 指定したノードが指定したビンに排他的に属するようにします。

    -----------------------------------------

    notifyChanged (boolean): このフラグを使用して、binMembershipが変更されたとこを通知します。

    -----------------------------------------

    removeFromBin (string): ノードリスト内のノードをビンから除去します。

    -----------------------------------------

    Return Value:
    None: booleanコマンドの結果照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def callbacks(addCallback: str = "",clearAllCallbacks: bool = False,clearCallbacks: bool = False,describeHooks: bool = False,dumpCallbacks: bool = False,executeCallbacks: bool = False,hook: str = "",listCallbacks: bool = False,owner: str = "",removeCallback: str = "") -> None:
    """
    このコマンドでは、Maya UI の作成時、キーの時間にコールバックを追加して UI を拡張できます。標準の Maya フックおよびコンテキストに応じてコールバックに渡す引数は、以下の「describeHooks」 UI を拡張するプラグインを追加するサード パーティもカスタム フックを追加できます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    addCallback (script): 指定したフックにコールバックを追加します。コールバックを追加する際にはオーナーも指定する必要があります。

    -----------------------------------------

    clearAllCallbacks (boolean): すべてのフックおよびオーナーのすべてのコールバックをクリアします。これは、Mayaおよび他のサードパーティが登録したすべてのコールバックに影響するため、通常プラグインの開発およびテスト時のみ使用します。

    -----------------------------------------

    clearCallbacks (boolean): 指定したオーナーのコールバックをすべてクリアします。フックを指定した場合は、そのフックのコールバックとオーナーのみがクリアされます。

    -----------------------------------------

    describeHooks (boolean): 標準のMayaフックをリストします。以下にフック、およびそれに関連付けられた引数と戻り値を示します。サードパーティによって追加されたカスタムフックはリストには含まれていません。hyperShadePanelBuildCreateMenuこのフックは、ハイパーシェードパネルの作成メニューにコンテンツを追加するためにコールされます。これは、標準のMayaノードエントリの作成後にコールされます。このコールバックには、引数や戻り値はありません。適切なMayaUIの外観を保持するには、menuItem-dividertrueを使用し、これらのコールバックが返される直前にメニュー項目分割を追加する必要があります。hyperShadePanelBuildCreateSubMenuこのフックは、標準のMayaノードとカスタムレンダラシェーディングノードを一緒にリストしない分類文字列を取得するためにコールされます。このコールバックには引数はありません。戻り値:次のような分類文字列rendernode/myrendererhyperShadePanelPluginChangeこのフックは、ハイパーシェードパネルを再構築する必要があることをMayaに通知する、プラグイン変更イベント(ロード/アンロード)が発生するとコールされます。classification(文字列):プラグインノードの分類文字列(別のプラグインのものである可能性もあります)changeType(文字列):loadPluginまたはunloadPluginのいずれ戻り値:(int)プラグインがこの分類のノードを対象としており、ハイパーシェードの再構築が必要な場合は0以外createRenderNodeSelectNodeCategoriesこのフックは、[レンダーノードの作成(CreateRenderNode)]ダイアログの構築時に、サードパーティのノードが既定で選択されることを許可する場合にコールされます。標準のフラグ形式は、-allWithMyRendererUpで、選択項目はコールバックのツリーリスタで設定できます。このコールバックには戻り値はありません。flag(文字列):[レンダーノードの作成(CreateRenderNode)]ダイアログコマンドに渡される、先頭のマイナス(-)を除去したフラグtreeLister(文字列):影響を受けるツリーリスタウィジェットたとえば、次のようなコールバックになります。globalprocmyRendererCreateRenderNodeSelectNodeCategoriesCallback(string$flag,string$treeLister){if($flag=="allWithMyRendererUp"){treeLister-e-selectPath"myrenderer"$treeLister;}}createRenderNodePluginChangeこのフックは、[レンダーノードの作成(CreateRenderNode)]ダイアログを閉じる必要があるかどうかを判断するプラグインの変更イベントが発生したときにコールされます。classification(文字列):プラグインノードの分類文字列(別のプラグインのものである可能性もあります)戻り値:(int)プラグインがこの分類のノードを対象としており、[レンダーノードの作成(CreateRenderNode)]ダイアログを閉じる必要がある場合は0以外renderNodeClassificationこのフックは、カスタムレンダラシェーディングノード用の分類文字列を取得するためにコールされます。これは、指定したノードタイプがプラグインレンダラに属するかどうかを判断するために使用されます。このコールバックには引数はありません。戻り値:次のような分類文字列rendernode/myrenderercreateRenderNodeCommandこのフックは、プラグインレンダラに、レンダラノードtreeListerおよびノードエディタからノードを作成する独自のコマンドを登録する機会を与えるためにコールされます。コールバックでは、問題のノードタイプの分類から自身のタイプであるかどうかを判断する必要があります。該当する場合、そのタイプの新しいノードを作成する適切なコマンドを返します。postCommand(文字列):作成コマンドの後に実行するコマンドtype(文字列):nodeType戻り値:(文字列)MEL作成コマンドbuildRenderNodeTreeListerContentこのフックは、プラグインレンダラに、レンダラノードツリーリスタにそのコンテンツを追加する機会を与えるためにコールされます。renderNodeTreeLister(文字列):レンダラノードツリーリスタpostCommand(文字列):作成後に実行するコマンドfilterString(文字列):フィルタのスペース区切りのリストAETemplateCustomContentこのフックは、ソースがAEdependNodeTemplateのノードにアトリビュートエディタのコンテンツを追加する機会をプラグインに与えるためにコールされます。nodeName(文字列):アトリビュートエディタが構築されているノードの名前firstConnectedShaderこのフックは、指定したシェーディングエンジンに接続された一次カスタムシェーダを判断するためにコールされます。nodeName(文字列):シェーディングエンジンの名前returns(文字列):存在する場合、カスタムシェーダの名前allConnectedShadersこのフックは、指定したシェーディングエンジンに接続されているすべてのシェーダを判断するためにコールされます。nodeName(文字列):シェーディングエンジンの名前戻り値(文字列):接続されているカスタムシェーダのコロン区切りのリスト(shader1:shader2:shader3)renderLayerPresetMenuこのフックはrenderLayerノードにプリセットを追加する機会をプラグインに与えるためにコールされます。nodeName(文字列):renderLayerノードの名前addBakingMenuItemsこのフックは、グローバルの[レンダー(Render)]>[ライティング/シェーディング(Lighting/Shading)]メニューにベイクメニュー項目を追加する機会をプラグインに与えるためにコールされます。menuItemAnchor(文字列):後ろに新しいベイクメニュー項目を挿入するmenuItemの名前。addVertexBakingMenuItemsこのフックは、グローバルの[ポリゴン(Polygon)]>[カラー(Color)]メニューにベイクメニュー項目を追加する機会をプラグインに与えるためにコールされます。addPrelightMenuItemsこのフックは、グローバルの[ポリゴン(Polygon)]>[カラーセットエディタ(ColorSetEditor)]メニューにプリライティングメニュー項目を追加する機会をプラグインに与えるためにコールされます。addRMBBakingMenuItemsこのフックは、右マウスボタンメニューにベイクメニュー項目を追加する機会をプラグインに与えるためにコールされます。objectName(文字列):右マウスボタンイベントが発生したオブジェクトの名前addMayaRenderingPreferencesこのフックはMayaの[レンダリングプリファレンス(RenderingPreferences)]セクションにカスタムプリファレンスを追加する機会をプラグインに与えるためにコールされます。updateMayaRenderingPreferencesこのフックはMayaの[レンダリングプリファレンス(RenderingPreferences)]セクションのカスタムプリファレンスを更新する機会をプラグインに与えるためにコールされます。addMayaMuscleMenuItemsこのフックは、Mayaマッスルの[ディスプレイスメント(Displace)]メニューにメニュー項目を追加する機会をプラグインに与えるためにコールされます。menuItemAnchor(文字列):後ろに新しいMayaマッスルメニュー項目を挿入するmenuItemの名前。addMayaMuscleShelfButtonsこのフックは、Mayaマッスルシェルフに項目を追加する機会をプラグインに与えるためにコールされます。addBackburnerRendererMenuItemsこのフックは、Mayaの利用可能なレンダラのBackburnerリストに項目を追加する機会をプラグインに与えるためにコールされます。注:追加したmenuItemの名前は、レンダラと同等にショートネームにする必要があります。例:Mayaソフトウェアレンダラによって「sw」という名前のmenuItemが追加されます。provideAETemplateForNodeTypeこのフックは、対応するAE'nodeType'Templateプロシージャを持たないノードにUIテンプレートを提供する機会をプラグインに与えるためにコールされます。nodeType(文字列):AEが構築されているノードのタイプ戻り値(文字列):要求されたノードタイプのAETemplateとして使用するMELコマンドまたはプロシージャの名前AEnewMultiHandlerこのフックは、マルチアトリビュートにUI作成ハンドラを提供する機会をプラグインに与えるためにコールされます。nodeName(文字列):AEが構築されているノードの名前atributeName(文字列):マルチアトリビュートの名前uiName(文字列):アトリビュートのUI名changedCommand(文字列):マルチアトリビュートの値を変更したときに実行されるMELコマンドまたはプロシージャelementIndexString(文字列):マルチアトリビュートの要素があるインデックスのコロン区切りのリスト戻り値(文字列):コールバックでアトリビュートを処理した場合、作成した最上位のUI要素のフルネームを返す必要があります。そうでない場合は、空の文字列を返す必要があります。AEreplaceMultiHandlerこのフックは、マルチアトリビュートに更新ハンドラを提供する機会をプラグインに与えるためにコールされます。layoutName(文字列):マルチアトリビュートを表すMayaUIコンポーネントの明確に定義された名前nodeName(文字列):AEが構築されているノードの名前atributeName(文字列):マルチアトリビュートの名前changedCommand(文字列):マルチアトリビュートの値を変更したときに実行されるMELコマンドまたはプロシージャelementIndexString(文字列):マルチアトリビュートの要素があるインデックスのコロン区切りのリスト戻り値(整数):コールバックでマルチアトリビュートを処理した場合は1、Mayaで既定の処理を提供する必要がある場合は0を返します。AEnewAttributeHandlerこのフックは、アトリビュートにUI作成ハンドラを提供する機会をプラグインに与えるためにコールされます。nodeName(文字列):AEが構築されているノードの名前atributeName(文字列):アトリビュートの名前uiName(文字列):アトリビュートのUI名changedCommand(文字列):アトリビュートの値を変更したときに実行されるMELコマンドまたはプロシージャ戻り値(文字列):コールバックでアトリビュートを処理した場合、作成した最上位のUI要素のフルネームを返す必要があります。そうでない場合は、空の文字列を返す必要があります。AEreplaceAttributeHandlerこのフックは、アトリビュートに更新ハンドラを提供する機会をプラグインに与えるためにコールされます。nodeName(文字列):AEが構築されているノードの名前atributeName(文字列):アトリビュートの名前changedCommand(文字列):アトリビュートの値を変更したときに実行されるMELコマンドまたはプロシージャ戻り値(整数):コールバックでアトリビュートを処理した場合は1、Mayaで既定の処理を提供する必要がある場合は0を返します。provideClassificationStringsこのフックは、「shader/surface」分類ネームスペースにノードを追加するすべてのサードパーティが指定する必要があります。戻り値(文字列):さまざまなプラグインノードの分類を表すコロン区切りのリストprovideClassificationExclusionStringsこのフックは、nodeTreeListerカテゴリから除外する必要がある分類のリストを提供する機会をプラグインに与えるためにコールされます。たとえば、プラグインは、「material」と「legacy」の両方に分類されたノードを「material」カテゴリから除外することができます。classification(文字列):nodeTreeBuilderが照会している分類戻り値(文字列):nodeTreeBuilderが照会している分類から除外する必要があるさまざまな分類を表すコロン区切りのリストprovideClassificationStringsForFilteredTreeListerこのフックは「createAssignNewMaterialTreeLister」によってコールされ、ツリーリスタビルダに渡される分類フィルタにアペンドする機会をプラグインに与えます。新しい分類がそれぞれ空白で区切られている文字列を返す必要があります。currentFilterString(文字列):現在の分類を表す、空白で区切られた文字列nodeCanBeUsedAsMaterialこのフックはRMBの[お気に入りのマテリアルの割り当て]メニューで使用され、マテリアルとして使用できるシェーディングノードを定義します。ノードをマテリアルノードとして使用できる場合は1、できない場合は0を返す必要があります。nodeId(文字列):照会するシェーディングノードのノードIDnodeOwner(文字列):ノードが属するプラグインの名前addHeaderContentToMayaLambertianShadersAEこのフックは、Mayaのランベルトから生じるシェーダのアトリビュートエディタのヘッダーにコンテンツを追加する機会をプラグインに与えるためにコールされます。nodeName(文字列):アトリビュートエディタが構築されているノードの名前provideNodeToAttrConnectionこのフックは、ノードが入力アトリビュートに接続される場合に、使用する出力アトリビュートをプラグインで指定するためにコールされます。入力アトリビュートタイプが与えられた場合、一致するタイプの出力アトリビュートを返す必要があります。アトリビュートタイプが指定されない場合(空の文字列)、任意のタイプの希望する出力アトリビュートを返すことができます。一致するタイプの出力アトリビュートが使用できない場合は、空の文字列が返されます。nodeType(文字列):照会されたノードのノードタイプattributeType(文字列):入力アトリビュートのデータタイプreturns(文字列):使用する出力アトリビュート名provideNodeToNodeConnectionこのフックは、ノード間の接続がなされた場合に、どのアトリビュートを接続するべきかをプラグインが提供する機会を与えるためにコールされます。ソースおよび目的のアトリビュートはどちらも、「src1:dst1:src2:dst2:src3:dst3」のようなコロン区切りのリストで返される必要があります。srcType(文字列):ソースノードのノードタイプdstType(文字列):目的のノードのノードタイプreturns(文字列):ソースおよび目的のアトリビュート名のコロン区切りのリストprovideOutputAttributeNameForTextureNodeこのフックは、テクスチャノードに異なる出力アトリビュート名を提供する機会をプラグインに与えるためにコールされます。このフックが提供されない場合、「outColor」が使用されます。nodeName(文字列):照会されるテクスチャノードの名前戻り値(文字列):テクスチャノードの出力アトリビュート名addItemsToHypergraphNodePopupMenuこのフックは、ハイパーグラフノードポップアップメニューに項目を追加する機会をプラグインに与えるためにコールされます。nodeName(文字列):ハイパーグラフノードメニューが構築されているノードの名前addItemsToRenderLayerEditorPopupMenuこのフックは、レンダーレイヤエディタポップアップメニューに項目を追加する機会をプラグインに与えるためにコールされます。layerName(string):ポップアップメニューが構築されているレンダーレイヤの名前preventMaterialDeletionFromCleanUpSceneCommandこのフックはcleanUpSceneコマンドによってコールされ、マテリアルノードが使用中で削除してはならないことを伝える機会をプラグインに与えます。フックは各シェーダインスタンスのプラグ/接続ペアごとに1回コールされます。shader(文字列):削除するシェーダノードの名前plug(文字列):照会されたプラグの名前connection(文字列):照会された接続の名前connectNodeToNodeOverrideCallbackこのフックは、ドラッグ＆ドロップの動作を再定義する機会をプラグインに与えるためにコールされます。srcNode(文字列):ソースノード(ドラッグしたノード)の名前dstNode(文字列):目的のノード(ドロップ先のノード)の名前戻り値(整数):この接続の結果として通常生じる操作をMayaが実行する必要がある場合は1を返します。オーバーライドしてカスタムの動作を提供する場合は0を返します。prepareRenderChangedこのフックは、prepareRenderコマンドで走査セットを編集した後に呼び出されます。enableRenderPassMenuOfRenderViewこのフックは、レンダービューのレンダーパスメニュー(ファイル>レンダーパスのロード(File>LoadRenderPass))を有効にする必要があることをMayaに指示する機会をプラグインに与えるためにコールされます。「addRenderPassMenuItemsToRenderView」を使用すると、このメニューに項目を追加することができます。戻り値(整数):プラグインでレンダービューのレンダーパスメニューを有効にする必要がある場合は1を返します。そうでない場合は0を返します。addItemsToRenderPassMenuOfRenderViewこのフックは、レンダービューの「レンダーパス」メニュー(ファイル>レンダーパスのロード(File>LoadRenderPass))にメニュー項目を追加する機会をプラグインに与えるためにコールされます。「enableRenderPassMenuOfRenderView」を使用すると、レンダービューのレンダーパスメニューを有効にすることができます。addItemsToRMBMenuOfTreeListerこのフックは、ツリーリスタにリストされているノードの右マウスボタンメニューを生成する機会をプラグインに与えるためにコールされます。プラグインは、右マウスボタンメニューに項目を追加する前に、メニュー項目分割(menuItem-dividertrueを使用)を追加する必要があります。nodeType(文字列):右マウスボタンメニューが構築されるツリーリスタノードのノードタイプscriptCommand(文字列):右マウスボタンメニューが構築されるツリーリスタノードに関連付けられたスクリプトコマンド戻り値(整数):Mayaが現在のノードタイプのメニューに独自の項目をアペンドする必要がある場合は0を返します。これは、プラグインが明示的に関係していないすべてのノードタイプの戻り値である必要があります。Mayaが現在のノードタイプのメニューに項目を追加しない場合は1を返します。注:ツリーリスタのお気に入り(Favorites)セクションの管理に関連するすべてのメニュー項目は、戻り値に関係なく常に右マウスボタンメニューに追加されます(これらは特殊なケースとして扱われます)。saveCustomNodePresetAttributesこのフックは、保存されるノードプリセットファイルに追加のコマンドを保存する機会をプラグインに与えるためにコールされます。presetNodeToSave(文字列):保存されるプリセットノードの名前。戻り値(文字列):現在のpresetNode保存イベントのnodePreset-customフラグにアペンドされるMELスクリプトを生成するために使用するカスタムプロシージャ(-customフラグのフォーマットの詳細についてはnodePresetコマンドのマニュアルを参照)addItemToFileMenuこのフックは、メインのファイルメニューにメニュー項目を追加する機会をプラグインに与えるためにコールされます。addItemToCreateLightMenuこのフックは、ライト作成(createlight)メニューにメニュー項目を追加する機会をプラグインに与えるためにコールされます。textureReloadこのフックは、テクスチャファイルを参照するすべてのノードを更新する機会をプラグインに与えるためにコールされます。ファイル(文字列):リロードするテクスチャファイルのパス。renderSettingsBuiltこのフックは、レンダー設定(RenderSettings)ウィンドウを作成した後に呼び出されます。rendererAddOneTabToGlobalsWindowCreateProcこのフックは、レンダラが、統一レンダーグローバル(RenderGlobals)ウィンドウ(レンダー設定ウィンドウ)に、レンダラ特有のタブを追加する機会を許可するために呼び出されます。createProc(文字列):タブのコンテンツの作成に使用するプロシージャの名前です。shouldEarlyReturnFromUpdateMultiCameraBufferNamingMenuこのフックを呼び出すと、コールバックハンドラで「true(真)」を返すことによって、updateMultiCameraBufferNamingMenu()関数の戻り値を早く返すことができます。戻り値(文字列):呼び出し元がupdateMultiCameraBufferNamingMenu()関数から戻り値を早く返すようにする場合は「true(真)」を返します。shouldEarlyReturnFromUpdateMayaSoftwareImageFormatControlこのフックを呼び出すと、コールバックハンドラで「true(真)」を返すことによって、updateMayaSoftwareImageFormatControl()関数の戻り値を早く返すことができます。戻り値(文字列):呼び出し元がupdateMayaSoftwareImageFormatControl()関数から戻り値を早く返すようにする場合は「true(真)」を返します。shouldEarlyReturnFromUpdateDefaultTraversalSetMenuこのフックを呼び出すと、コールバックハンドラで「true(真)」を返すことによって、updateDefaultTraversalSetMenu()関数の戻り値を早く返すことができます。戻り値(文字列):呼び出し元がupdateDefaultTraversalSetMenu()関数から戻り値を早く返すようにする場合は「true(真)」を返します。shouldEarlyReturnFromShouldAppearInNodeCreateUIこのフックを呼び出すと、コールバックハンドラで「true(真)」を返して、shouldAppearInNodeCreateUI()関数の戻り値を早く返すことができます。戻り値(文字列):呼び出し元がshouldAppearInNodeCreateUI()関数から戻り値を早く返すようにする場合は「true(真)」を返します。updateAEこのフックは、updateAE()関数の終了時点で呼び出されます。

    -----------------------------------------

    dumpCallbacks (boolean): すべてのフックおよびオーナーによって登録されたすべてのコールバックのリストを取得できます。デバッグに便利です。

    -----------------------------------------

    executeCallbacks (boolean): 指定したフックのコールバックを、実行時に追加の引数を各コールバックに渡しながら実行します。実行された各コールバックの戻り値を含む配列(MEL)またはリスト(Python)を返します。コールバックが値を返さない場合、配列は空の文字列(MEL)またはNone(Python)になります。

    -----------------------------------------

    hook (string): コールバックを登録するフックの名前。

    -----------------------------------------

    listCallbacks (boolean): 指定したフック名のコールバックのリストを取得します。オーナーを指定した場合は、指定したフックのコールバックとオーナーのみがリストされます。

    -----------------------------------------

    owner (string): コールバックを登録するオーナーの名前。これは通常はプラグイン名になります。

    -----------------------------------------

    removeCallback (script): 指定したフック名の既存のコールバックを除去します。コールバックを除去する際にはオーナーも指定する必要があります。

    -----------------------------------------

    Return Value:
    None: string[]コマンドの結果
    """
    pass

    
def checkDefaultRenderGlobals() -> None:
    """
    最後にファイルを保存してから defaultRenderGlobals ノードが変更されたかどうかを照会するには、`ls -modified` を使用します。シーンを強制的にダーティまたはクリーンにするには、`file -modified` を使用します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def convertSolidTx(alpha: bool = False,antiAlias: bool = False,backgroundColor: Tuple[int, int, int] = tuple(1, 1, 1),backgroundMode: str = "",camera: str = "",componentRange: bool = False,doubleSided: bool = False,fileFormat: str = "",fileImageName: str = "",fillTextureSeams: bool = False,force: bool = False,fullUvRange: bool = False,name: str = "",pixelFormat: str = "",resolutionX: int = 1,resolutionY: int = 1,reuseDepthMap: bool = False,samplePlane: bool = False,samplePlaneRange: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),shadows: bool = False,uvBBoxIntersect: bool = False,uvRange: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),uvSetName: str = "") -> None:
    """
    サーフェスのテクスチャをファイル テクスチャに変換するコマンド。最初の引数はレンダリング ノードまたはアトリビュートです。ノードのみが指定された場合、outColor アトリビュートがサンプリングされます。ノードに outColor アトリビュートがない場合は、ノードの最初のアトリビュートが使用されます。ノードは、読み取りはできるが書き込みはできず、隠しノードではなく、接続可能で多色の縞模様ではないものです。ライティングをベイク処理する場合、シェーディング グループをテクスチャとして指定する必要があります。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    alpha (boolean): ライティングをベイク処理する際に透明度を計算するかどうかを指定します。変換では、シェーディングネットワークのカラーと透明度の両方がサンプリングされます。ファイルテクスチャのアルファチャネルは、透明度のサンプリング結果に合わせて設定されます。既定では透明度は計算されません。

    -----------------------------------------

    antiAlias (boolean): 作成されたイメージでアンチエイリアシングを行います。ソリッドテクスチャを変換すると、アンチエイリアシングなしに比べて、通常4倍の時間がかかります。既定ではこのフラグはオフです。

    -----------------------------------------

    backgroundColor ([int, int, int]): バックグラウンドカラーを特定の値に設定します。既定では、シェーダの既定のカラーを使ってバックグラウンドを塗り潰します。ピクセルフォーマットがチャネルあたり8ビットの場合、有効な値の範囲は0～255で、ピクセルフォーマットがチャネルあたり16ビットの場合、0～65535です。このフラグは自動的に-backgroundModeを「color」に設定します。既定は黒の000.

    -----------------------------------------

    backgroundMode (string): テクスチャのバックグラウンドを塗りつぶす方法を定義します。次の3つのモードが利用できます:「shader」または1:既定のシェーダカラーを使用します。「color」または2:-backgroundColorフラグで指定したカラーを使用します。「extend」または3:継ぎ目のエッジのカラーを外側に拡大します。既定は「shader」です。

    -----------------------------------------

    camera (name): ライティングのベイク処理で使用するカメラを指定します。カメラを指定していない場合は、アクティブなビューのカメラが使用されます。

    -----------------------------------------

    componentRange (boolean): 1つまたは複数のコンポーネントを使用するように選択し、このフラグを設定している場合、コンポーネントのuv範囲を使用してテクスチャマップの解像度に合わせられます。既定ではこのフラグはfalseに設定されています。

    -----------------------------------------

    doubleSided (boolean): サンプルポイントがカメラと逆の位置にある場合、サンプラがサーフェス法線を反転するかどうかを指定します。注:法線を反転すると、カメラによって結果が異なります（つまり、同じ場所でも法線を反転するカメラと反転しないカメラがあります）。doubleSidedをシャドウと組み合わせて使用することはお勧めしません。既定ではこのフラグはfalseです。

    -----------------------------------------

    fileFormat (string): 出力に使用されるファイルフォーマット。指定しない場合は、IFFが既定設定です。その他の有効なフォーマットは、次のとおりです。als:AliasPIXcin:Cineoneps:EPSgif:GIFiff:MayaIFFjpg:JPEGyuv:Quantelrla:WavefrontRLAsgi:SGIsi:SoftImage(.pic)tga:Targatif:TIFFbmp:WindowsBitmap

    -----------------------------------------

    fileImageName (string): ファイルテクスチャイメージの出力パスと名前を指定します。ファイル名にディレクトリセパレータが含まれない場合、イメージは現在のプロジェクトのソースイメージに書き込まれます。ファイルがすでに存在するとき、バージョン設定は行われません。

    -----------------------------------------

    fillTextureSeams (boolean): ファイルテクスチャを作成するときに、テクスチャの継ぎ目を埋めるために外側のエッジを越えてポリゴンをオーバースキャンするかどうかを指定します。既定はtrueです。

    -----------------------------------------

    force (boolean): 出力イメージがすでに存在している場合は、上書きされます。既定ではこのフラグはオフです。

    -----------------------------------------

    fullUvRange (boolean): サーフェスのUV範囲全体を使用してサンプリングします。このフラグは、-uvrフラグと同時には使用できません。2Dテクスチャ配置ノードが作成され、ファイルテクスチャに接続されます。配置の移動と有効範囲が、サーフェスのUV範囲全体に従って設定されます。

    -----------------------------------------

    name (string): ファイルテクスチャノードの名前が設定されます。複数のオブジェクトを指定するときは、名前が衝突した場合の解決法を使用して有効な名前が決定されます。

    -----------------------------------------

    pixelFormat (string): イメージのピクセルフォーマットを指定します。すべてのファイルフォーマットですべてのピクセルフォーマットをサポートしていないことに注意してください。有効なオプション:「8」:チャネルあたり8ビット、符号なし(0～255)「16」:チャネルあたり16ビット、符号なし(0～65535)既定は「8」です。

    -----------------------------------------

    resolutionX (int): 水平イメージ解像度を設定します。このフラグを指定しないと、解像度は256に設定されます。

    -----------------------------------------

    resolutionY (int): 垂直イメージ解像度を設定します。このフラグを指定しないと、解像度は256に設定されます。

    -----------------------------------------

    reuseDepthMap (boolean): 作成されたすべての深度マップを再使用するかどうかを指定します。既定はfalseです。

    -----------------------------------------

    samplePlane (boolean): バーチャルプレーンを使ってサンプリングするかどうかを指定します。このバーチャルプレーンでは、-samplePlaneRangeフラグによって定義された長方形内にテクスチャ座標があります。-samplePlaneRangeフラグが設定されない場合は、既定でバーチャルプレーンの(0,0)から(1,1)の正方形内にテクスチャ座標が設定されます。このオプションが設定されていると、すべての引数ベースのサーフェスは無視されます。

    -----------------------------------------

    samplePlaneRange ([float, float, float, float]): -samplePlaneオプションが設定されている場合に、サンプリングに使用するテクスチャ座標のUV範囲を指定します。uMin、uMax、vMin、vMaxに対応する4つの引数があります。既定でバーチャルプレーンは、uMin0からuMax1とvMin0からvMax1になります。

    -----------------------------------------

    shadows (boolean): ライティングをベイク処理する際にシャドウを計算するかどうかを指定します。ディスクベースのシャドウマップが使用されます。深度マップシャドウ付きのライトのみを有効にすると、シェーディングに役立ちます。既定ではシャドウは計算されません。

    -----------------------------------------

    uvBBoxIntersect (boolean): このフラグは現在サポートしていません。

    -----------------------------------------

    uvRange ([float, float, float, float]): サンプルを計算するUV範囲を指定します。uMin、uMax、vMin、vMaxに対応する4つの引数があります。それぞれの値は、サーフェスのUV空間に基づいて指定する必要があります。2Dテクスチャ配置ノードが作成され、ファイルテクスチャに接続されます。配置のフレームの移動と有効範囲が指定したUV範囲に従って設定されます。既定ではサーフェスのUV範囲全体が使用されます。

    -----------------------------------------

    uvSetName (string): ソリッド変換用のドライビングパラメータ設定として使用する必要があるUV設定を指定します。

    -----------------------------------------

    Return Value:
    None: string[]ファイル テクスチャ ノード照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def convertTessellation(allCameras: bool = False,camera: str = "") -> None:
    """
    基本のテッセレーション アトリビュートを高度なアトリビュートに変換するコマンド。カメラ フラグが指定されている場合、サーフェスとカメラの距離に基づいて変換されます。サーフェスとカメラの距離が近いほど、テッセレーションに含まれる三角形の数が増えます。「-allCameras」フラグを指定すると、サーフェスに最近接のレンダリング可能なカメラを使用してテッセレーションが設定されます。カメラのテッセレーション推定値は現在のレンダー解像度にも依存します。解像度が高いほど、サーフェスのテッセレーションがよりきめ細かくなります。複数の NURB サーフェスをコマンド ラインで指定でき、またはコマンドの引数を指定しない場合は、アクティブ リストが使用されます。このコマンドは、サーフェスのレンダー時にテッセレーションがスムーズになるよう、弦の高さを計算します。高度なテッセレーション設定は、指定した各サーフェスで有効になり、一次テッセレーション パラメータが設定され、弦の高さが二次基準として使用されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    allCameras (boolean): スクリーンベースのテッセレーションを計算する場合に使用するすべてのレンダリング可能なカメラを指定します。

    -----------------------------------------

    camera (name): スクリーンベースのテッセレーションを計算する場合に使用するカメラを指定します。

    -----------------------------------------

    Return Value:
    None: boolean成功または失敗
    """
    pass

    
def displacementToPoly(findBboxOnly: bool = False) -> None:
    """
    このコマンドを使用して、ジオメトリをディスプレイスメント マッピングでポリゴン オブジェクトへとベイク処理します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    findBboxOnly (boolean): ディスプレイスメントされたオブジェクトのバウンディングボックスのスケールのみが検索されます。

    -----------------------------------------

    Return Value:
    None: boolean成功または失敗照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def doBlur(colorFile: str = "",length: float = 1.0,memCapSize: float = 1.0,sharpness: float = 1.0,smooth: float = 1.0,smoothColor: bool = False,vectorFile: str = "") -> None:
    """
    Maya のスタンドアロン型アプリケーションである blur2d が起動され、指定したカラー イメージとモーション ベクトル ファイルで 2.5 モーション ブラーが実行されます。入力 colorFile 名としてたとえば「xxx.iff」を指定した場合、出力ブラー イメージは、入力 colorFile と同じディレクトリの「xxx_blur.iff」になります。出力ブラー イメージの名前は現在制御できません。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    colorFile (string): ブラーをかける入力カラーイメージの名前。

    -----------------------------------------

    length (float): モーションベクトルに適用されたスケール。範囲は0から無限です。

    -----------------------------------------

    memCapSize (float): バイト単位のメモリキャップのサイズです。

    -----------------------------------------

    sharpness (float): ブラーフィルタのシェイプを決めます。値が大きいとフィルタは狭くなり、ブラーはシャープになります。値が小さいとフィルタは広くなり、ブラーは広がります。範囲は0から無限です。

    -----------------------------------------

    smooth (float): ブラーイメージを滑らかにするフィルタサイズ。値を大きくすると、アルファチャネルのアンチエイリアシングの度合いが強くなります。範囲は1.0から5.0です。

    -----------------------------------------

    smoothColor (boolean): カラーをスムーズにするかどうか。

    -----------------------------------------

    vectorFile (string): 入力モーションベクトルファイルの名前。

    -----------------------------------------

    Return Value:
    None: stringコマンドの結果
    """
    pass

    
def getRenderDependencies() -> None:
    """
    イメージ ソースの依存関係を返すコマンドです。イメージ ソース(レンダー ターゲットなど)は、3D シーンのレンダリングまたは 2D 合成グラフのレンダリングから生じた他の上流のイメージ ソースに依存する可能性があります。このコマンドはこれらの依存関係を返すため、それを分析してンダリングできます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    Return Value:
    None: string引数イメージ ソースの依存関係
    """
    pass

    
def getRenderTasks(camera: str = "",renderLayer: str = "") -> None:
    """
    イメージ ソースをレンダーするレンダー タスクを返すコマンドです。イメージ ソースは、3D シーンまたは 2D レンダリング(レンダー ターゲットなど)のレンダリングから生じる上流のイメージ ソースに依存する可能性があります。このコマンドはイメージ ソースのレンダー依存関係のグラフを取得し、その依存関係に従ってレンダー タスクを作成します。レンダー タスクには、カメラ、レンダー レイヤ、解像度などレンダラー固有のコンテキストがあります。イメージ ソースのオーバーライドのため、レンダー タスクのコンテキストは、適用されるコンテキスト項目の最上流のオーバーライドと共に、レンダーのディペンデンシー グラフのパスに依存します。レンダーのディペンデンシー グラフのパスは複数あることがあるため、指定したレンダーの依存関係には複数のタスクがある可能性があります。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    camera (string): イメージソースレンダータスクのレンダーコンテキストで使用するカメラノードです。

    -----------------------------------------

    renderLayer (string): イメージソースレンダータスクのレンダーコンテキストで使用するレンダーレイヤです。

    -----------------------------------------

    Return Value:
    None: string[]引数レンダー ターゲットのレンダー タスク(文字列単位)。
    """
    pass

    
def glRender(accumBufferPasses: int = 1,alphaSource: str = "",antiAliasMethod: str = "",cameraIcons: bool = False,clearClr: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),collisionIcons: bool = False,crossingEffect: bool = False,currentFrame: bool = False,drawStyle: str = "",edgeSmoothness: float = 1.0,emitterIcons: bool = False,fieldIcons: bool = False,flipbookCallback: str = "",frameEnd: int = 1,frameIncrement: int = 1,frameStart: int = 1,fullResolution: bool = False,grid: bool = False,imageDirectory: str = "",imageName: str = "",imageSize: Tuple[int, int, float] = tuple(1, 1, 1.0),lightIcons: bool = False,lightingMode: str = "",lineSmoothing: bool = False,offScreen: bool = False,renderFrame: str = "",renderSequence: str = "",sharpness: float = 1.0,shutterAngle: float = 1.0,textureDisplay: bool = False,transformIcons: bool = False,useAccumBuffer: bool = False,viewport: Tuple[int, int, float] = tuple(1, 1, 1.0),writeDepthMap: bool = False) -> None:
    """
    このコマンドで、HRM (Hardware Render Manager)にアクセスできます。Maya の HRM は 1 つだけです。HRM はハードウェア レンダー バッファ ウィンドウで実行されるレンダリングを制御します。このコマンドによりシェル スクリプトは、レンダー状態を修正したり、レンダー要求を開始したりすることができます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    accumBufferPasses (int): アキュムレーションバッファレンダーパスの数を設定します。

    -----------------------------------------

    alphaSource (string): イメージファイルの書き込み時にアルファソースをコントロールします。有効な値は次のとおりです。off、alpha、red、green、blue、luminance、clamp、invClamp。

    -----------------------------------------

    antiAliasMethod (string): ポリゴンのアンチエイリアシングで使用するメソッドを次のいずれかに設定します。off、uniform、gaussian。

    -----------------------------------------

    cameraIcons (boolean): カメラアイコンの表示状態を設定します。

    -----------------------------------------

    clearClr ([float, float, float]): ビューポートクリアカラーを設定します(0-1)。

    -----------------------------------------

    collisionIcons (boolean): 衝突モデルアイコンの表示状態を設定します。

    -----------------------------------------

    crossingEffect (boolean): 渦巻きフィルタを使用したイメージのフィルタリングを有効または無効にします。

    -----------------------------------------

    currentFrame (boolean): レンダーしている現在のフレームを返します。

    -----------------------------------------

    drawStyle (string): オブジェクトの描画スタイルを次のいずれかに設定します。boundingbox、points、wireframe、flatShaded、smoothShaded。

    -----------------------------------------

    edgeSmoothness (float): エッジのスムージング量を制御します。値が0.0ではスムージングは行われません。既定のスムージングは1.0で、それ以外の値を入力すると既定のスムージング量に応じてスケールされます。アキュムレーションバッファを有効にしておく必要があります。

    -----------------------------------------

    emitterIcons (boolean): エミッタアイコンの表示状態を設定します。

    -----------------------------------------

    fieldIcons (boolean): フィールドアイコンの表示状態を設定します。

    -----------------------------------------

    flipbookCallback (string): レンダーシーケンスの完了後に、プロシージャをコールできるように登録します。フリップブックプルダウンメニューを構築するために使用します。このプロシージャの構築方法についての詳細は、以下の例を参照してください。

    -----------------------------------------

    frameEnd (int): レンダーする終了フレームを設定します。

    -----------------------------------------

    frameIncrement (int): レンダリング時のフレームの増分を設定します。

    -----------------------------------------

    frameStart (int): レンダーする開始フレームを設定します。

    -----------------------------------------

    fullResolution (boolean): イメージ出力のフル解像度でのレンダリングを有効または無効にします。有効なイメージ出力解像度を設定する必要があります(-is)。

    -----------------------------------------

    grid (boolean): グリッドの表示状態を設定します。

    -----------------------------------------

    imageDirectory (string): イメージファイルのディレクトリを設定します。

    -----------------------------------------

    imageName (string): イメージファイルのベース名を設定します。

    -----------------------------------------

    imageSize ([int, int, float]): イメージ出力サイズを設定します。幅、高さ、アスクペクト比を設定します。0、0、0を渡すと現在のポートサイズを使用します。イメージサイズはビューポートサイズと同じから、それ以上である必要があります。フル解像度でのレンダリングが有効になっている場合、大きなイメージはタイル表示になります(-fr/fullResolution)。

    -----------------------------------------

    lightIcons (boolean): ライトアイコンの表示状態を設定します。

    -----------------------------------------

    lightingMode (string): レンダリングで使用するライティングモードを次のいずれかに設定します。all、selected、default。

    -----------------------------------------

    lineSmoothing (boolean): アンチエイリアシングしたラインを有効または無効にします。

    -----------------------------------------

    offScreen (boolean): 設定されている場合、HRMでオフスクリーンバッファを使用して、ビューをレンダーできるようになります。これにより、アプリケーションがアイコン化されているか、覆い隠されている場合に、HRMを動作させることができます。

    -----------------------------------------

    renderFrame (string): 現在のフレームをレンダーします。レンダーを行うビューの名前を要求します。

    -----------------------------------------

    renderSequence (string): 現在のフレームのシーケンスをレンダーします。レンダーを行うビューの名前を要求します。

    -----------------------------------------

    sharpness (float): 渦巻きフィルタの鮮明度をコントロールします。

    -----------------------------------------

    shutterAngle (float): モーションブラーで使用するシャッター角度を設定します(0-1)。値を0.0にするとブラーなし、0.5にすると正しいブラー、1.0にすると連続ブラーが使用されます。アキュムレーションバッファを有効にしておく必要があります。

    -----------------------------------------

    textureDisplay (boolean): テクスチャマップ表示を有効または無効にします。

    -----------------------------------------

    transformIcons (boolean): トランスフォームアイコンの表示状態を設定します。

    -----------------------------------------

    useAccumBuffer (boolean): アキュムレーションバッファを有効または無効にします。

    -----------------------------------------

    viewport ([int, int, float]): ビューポートサイズを設定します。幅、高さ、、アスクペクト比を渡します。このサイズは、フル解像度(-fr)と有効なイメージ出力サイズ(-is)を設定しない限り、すべてのテストレンダリングとイメージ出力サイズに使用されます。

    -----------------------------------------

    writeDepthMap (boolean): イメージファイルへのZ深度の書き込みを有効または無効にします。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def glRenderEditor(control: bool = False,defineTemplate: str = "",docTag: str = "",exists: bool = False,filter: str = "",forceMainConnection: str = "",highlightConnection: str = "",lockMainConnection: bool = False,lookThru: str = "",mainListConnection: str = "",panel: str = "",parent: str = "",selectionConnection: str = "",stateString: bool = False,unParent: bool = False,unlockMainConnection: bool = False,updateMainConnection: bool = False,useTemplate: str = "",viewCameraName: bool = False) -> None:
    """
    glRender ビューを作成します。これはハードウェア レンダリングで使用する特殊なビューです。このコマンドは、ビューを作成し、パネルのサポートに必要な再ペアレント化するために使用します。ハードウェア レンダリングの特定の動作のコントロールについては、glRender コマンドを参照してください。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    control (boolean): 照会モード専用です。このエディタの最上位のコントロールを返します。通常は、親を取得してポップアップメニューをアタッチするために使用します。注意:コントロールのないエディタが存在する場合があります。コントロールが存在しない場合は、この照会はNONEを返します。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    docTag (string): エディタにタグをアタッチします。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    filter (string): このエディタに使用する項目フィルタオブジェクトの名前を指定します。エディタの主要リストに表示される情報をフィルタします。

    -----------------------------------------

    forceMainConnection (string): エディタがコンテンツのソースとして使用するselectionConnectionオブジェクトの名前を指定します。エディタはselectionConnectionオブジェクトに含まれている項目のみを表示します。これは-mainListConnectionフラグの変形で、接続がロックされている場合でも強制的に変更します。このフラグを使用して、-unlockMainConnection、-mainListConnection、-lockMainConnectionフラグを直後に連続して使用する場合に、オーバーヘッドを減します。

    -----------------------------------------

    highlightConnection (string): そのハイライトリストをエディタと同期化させるselectionConnectionオブジェクトの名前を指定します。すべてのエディタにハイライトリストがあるわけではありません。ハイライトリストがあるエディタの場合、これは第二の選択項目を表示したリストになります。

    -----------------------------------------

    lockMainConnection (boolean): mainConnection内のオブジェクトの現在のリストをロックして、そのオブジェクトだけがエディタ内に表示されるようにします。これ以降、元のmainConnectionに変更を加えても無視されます。

    -----------------------------------------

    lookThru (string): glRenderビューが使用するカメラを指定します。

    -----------------------------------------

    mainListConnection (string): エディタがコンテンツのソースとして使用するselectionConnectionオブジェクトの名前を指定します。エディタはselectionConnectionオブジェクトに含まれている項目のみを表示します。

    -----------------------------------------

    panel (string): このエディタ用のパネルを指定します。既定では、エディタがスクリプトパネルの作成コールバックで作成された場合、エディタはそのパネルに属します。エディタがパネルに属していない場合、エディタのあるウィンドウを削除するとエディタも削除されます。

    -----------------------------------------

    parent (string): このエディタの親のレイアウトを指定します。このフラグは、エディタが現在ペアレント化されていない場合のみに効果があります。

    -----------------------------------------

    selectionConnection (string): その独自のセレクションリストをエディタと同期化させるselectionConnectionオブジェクトの名前を指定します。このエディタから選択する場合、selectionConnectionオブジェクトの中から選択します。オブジェクトが変更されると、エディタが更新されて変更が反映されます。

    -----------------------------------------

    stateString (boolean): 照会モード専用のフラグです。エディタを作成して現在のエディタの状態と一致させるMELコマンドを返します。返されたコマンド文字列は、指定した名前の代わりに文字列変数$editorNameを使用します。

    -----------------------------------------

    unParent (boolean): エディタをそのレイアウトから除去するように指定します。これは照会モードでは使用できません。

    -----------------------------------------

    unlockMainConnection (boolean): mainConnectionをロック解除して、オリジナルのmainConnection(まだ使用可能な場合)を効率的に復元し、ダイナミックな更新を行います。

    -----------------------------------------

    updateMainConnection (boolean): ロックされたmainConnectionをオリジナルのmainConnectionから更新させますが、ロック状態は保持されます。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    viewCameraName (boolean): glRenderPanelで使用する現在のカメラ名を返します。これは照会専用フラグです。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def hwReflectionMap(backTextureName: str = "",bottomTextureName: str = "",cubeMap: bool = False,decalMode: bool = False,enable: bool = False,frontTextureName: str = "",leftTextureName: str = "",rightTextureName: str = "",sphereMapTextureName: str = "",topTextureName: str = "") -> None:
    """
    このコマンドは、hwReflectionMap ノードを作成してテクスチャされたサーフェスに反射をつけます。これらのサーフェスでは、現在、boolean アトリビュートの displayHWEnvironment が true に設定されています。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    backTextureName (string): このフラグは、立方体の後面のファイルテクスチャ名を指定します。既定はnoneです。照会するとstringを返します。

    -----------------------------------------

    bottomTextureName (string): このフラグは、立方体の下面のファイルテクスチャ名を指定します。既定はnoneです。照会するとstringを返します。

    -----------------------------------------

    cubeMap (boolean): オンの場合、テクスチャの反射は立方体マッピングを使って作成されます。既定はfalseです。反射は球マッピングを使って作成されます。照会するとbooleanを返します。

    -----------------------------------------

    decalMode (boolean): オンの場合、反射カラーがサーフェスシェーディングを置き換えます。既定はfalseです。反射はサーフェスシェーディングに乗算されます。照会するとbooleanを返します。

    -----------------------------------------

    enable (boolean): オンの場合、対応するhwReflectionMapノードが有効になります。既定はfalseです。照会するとbooleanを返します。

    -----------------------------------------

    frontTextureName (string): このフラグは、立方体の前面のファイルテクスチャ名を指定します。既定はnoneです。照会するとstringを返します。

    -----------------------------------------

    leftTextureName (string): このフラグは、立方体の左側面のファイルテクスチャ名を指定します。既定はnoneです。照会するとstringを返します。

    -----------------------------------------

    rightTextureName (string): このフラグは、立方体の右側面のファイルテクスチャ名を指定します。既定はnoneです。照会するとstringを返します。

    -----------------------------------------

    sphereMapTextureName (string): このフラグは、球マッピングオプションのファイルテクスチャ名を指定します。既定はnoneです。照会するとstringを返します。

    -----------------------------------------

    topTextureName (string): このフラグは、立方体の上面のファイルテクスチャ名を指定します。既定はnoneです。照会するとstringを返します。

    -----------------------------------------

    Return Value:
    None: string(作成された hwReflectionMap ノード名)照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def hwRender(acceleratedMultiSampleSupport: bool = False,activeTextureCount: bool = False,camera: str = "",currentFrame: bool = False,currentView: bool = False,edgeAntiAliasing: Tuple[int, int] = tuple(1, 1),fixFileNameNumberPattern: bool = False,frame: float = 1.0,fullRenderSupport: bool = False,height: int = 1,imageFileName: bool = False,layer: str = "",limitedRenderSupport: bool = False,lowQualityLighting: bool = False,noRenderView: bool = False,notWriteToFile: bool = False,printGeometry: bool = False,renderHardwareName: bool = False,renderRegion: Tuple[int, int, int, int] = tuple(1, 1, 1, 1),renderSelected: bool = False,textureResolution: int = 1,width: int = 1,writeAlpha: bool = False,writeDepth: bool = False) -> None:
    """
    ハードウェア レンダリング エンジンを使用してイメージまたはシーケンスをレンダーします。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    acceleratedMultiSampleSupport (boolean): このフラグを照会と一緒に使用した場合は、グラフィックスカードがハードウェアアクセラレータ付きマルチサンプリングをサポートしているかどうかを返します。

    -----------------------------------------

    activeTextureCount (boolean): このフラグを照会と一緒に使用した場合は、ハードウェアレンダラがグラフィック化したテクスチャの数を返します。

    -----------------------------------------

    camera (string): 使用するカメラを指定します。指定のカメラが見つからない場合は、使用可能な最初のカメラを使用します。

    -----------------------------------------

    currentFrame (boolean): 現在のフレームをレンダーします。

    -----------------------------------------

    currentView (boolean): オンにすると、現在選択しているビューのみがレンダーされます。

    -----------------------------------------

    edgeAntiAliasing ([uint, uint]): マルチパスレンダリングを有効にします。フレーム単位でレンダーされるコマ数のコントロールが、関連する2つのフラグ引数という形で提供されます。1番目の引数には、次に示すサンプリングアルゴリズムを指定します。0-UniformWeightedGridSampling1-RotatedGridSuperSampling(RGSS)2-GaussianWeightedSampling上記以外のサンプリング方法を使用すると、既定のサンプリング方法であるUniformWeightedGridSamplingが使用されます。2番目の引数には、使用するサンプル数を指定します。サンプリングアルゴリズムごとに、次に示す使用可能なサンプル数の固定セットがあります。0-UniformWeightedGridSampling1345791625361-RotatedGridSuperSampling(RGSS)1452-GaussianWeightedSampling134579162536特定のサンプリング方法で使用できるサンプル数以外の数を使用すると、既定のサンプル数である5が使用されます。このコマンドを介して渡された値が、ハードウェアレンダーグローバルノードに格納された設定をオーバーライドします。

    -----------------------------------------

    fixFileNameNumberPattern (boolean): このフラグを使用して、hardwareRenderGlobalsのファイル名を初期のファイル名パターンとし、ファイル名のフレーム番号のパターンを独自の方法で修正して、さらに新しいファイル名パターンを返すようにすることができます。hardwareRenderGlobalsのファイル名は変更されません。

    -----------------------------------------

    frame (float): レンダーするフレームを指定します。

    -----------------------------------------

    fullRenderSupport (boolean): このフラグを使用してコンテキストを作成、または照会することができます。コンテキストの作成では、ハードウェアのサポートが不十分であれば、レンダリングを中止してフレームをレンダーしません。コンテキストの照会では、現在使用しているグラフィックスシステムが最高画質のレンダリングをサポートしているかどうかを返します。制限付きサポート範囲については、グラフィックスカードの動作確認一覧表を参照してください。

    -----------------------------------------

    height (uint): 高さ(Height)このフラグを使用しない場合、高さはレンダーグローバル(RenderGlobals)設定から取得されます。

    -----------------------------------------

    imageFileName (boolean): このフラグを使用して、指定したフレームのイメージファイル名を照会することができます。フレームは「-frame」フラグを使って指定することができます。「-frame」を使用しない場合、現在のフレームの番号が使用されます。

    -----------------------------------------

    layer (name): 指定したレンダーレイヤをレンダーします。レンダーレイヤのレンダリング可能なアトリビュート値にかかわらず、このレンダーレイヤのみをレンダーします。レイヤ名は出力イメージファイル名にアペンドされます。指定したレンダーレイヤは、レンダリング前に現在のレンダーレイヤになり、レンダリング後も現在のレンダーレイヤのままです。

    -----------------------------------------

    limitedRenderSupport (boolean): このフラグを照会と一緒に使用すると、現在使用しているグラフィックスシステムが制限付きレンダリングをサポートしているかどうかを返します。制限付きサポートの最新の定義については、グラフィックスカードの動作確認一覧表を参照してください。

    -----------------------------------------

    lowQualityLighting (boolean): ピクセル(フラグメント)単位のライティング評価を無効にします。注:このコマンドを介して渡された値が、ハードウェアレンダーグローバルノードに格納された設定をオーバーライドします。

    -----------------------------------------

    noRenderView (boolean): オンにすると、イメージの計算後にレンダービューが更新されません。

    -----------------------------------------

    notWriteToFile (boolean): ファイルにイメージを書き込まない場合は、このフラグをtrueに設定します。それ以外の場合は、falseに設定します。このフラグの既定値は「false」です。

    -----------------------------------------

    printGeometry (boolean): ジオメトリオブジェクトが移動するにつれて、これを出力します。

    -----------------------------------------

    renderHardwareName (boolean): このフラグは、グラフィックスコンテキストを作成して、使用中のグラフィックスハードウェアの名前を返します。グラフィックスハードウェアは、オフスクリーンバッファの作成とOpenGLからのGL_RENDERER文字列の照会によって決定されます。オフスクリーンバッファが作成されなかった場合は、空の文字列が返されます。

    -----------------------------------------

    renderRegion ([uint, uint, uint, uint]): 領域をレンダー(RenderRegion)パラメータは4つの整数であり、範囲の左右上下を示します。

    -----------------------------------------

    renderSelected (boolean): 選択したオブジェクトのみをレンダーします。

    -----------------------------------------

    textureResolution (uint): ベイク処理されたテクスチャの解像度を指定します。

    -----------------------------------------

    width (uint): 幅(Width)このフラグを使用しない場合、幅はレンダーグローバル(RenderGlobals)設定から取得されます。

    -----------------------------------------

    writeAlpha (boolean): カラーバッファのアルファチャネルを読み込み、tifファイルとして返します。

    -----------------------------------------

    writeDepth (boolean): 深度バッファを読み込み、tifファイルとして返します。

    -----------------------------------------

    Return Value:
    None: booleanコマンドの結果照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def hwRenderLoad() -> None:
    """
    ハードウェア レンダーのダイナミック ロードを強制するために使用する空のコマンドです。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    Return Value:
    None: なし
    """
    pass

    
def iprEngine(copy: str = "",defineTemplate: str = "",diagnostics: bool = False,estimatedMemory: bool = False,exists: bool = False,iprImage: str = "",motionVectorFile: bool = False,object: str = "",region: Tuple[int, int, int, int] = tuple(1, 1, 1, 1),relatedFiles: bool = False,releaseIprImage: bool = False,resolution: bool = False,scanlineIncrement: str = "",showProgressBar: bool = False,startTuning: bool = False,stopTuning: bool = False,underPixel: Tuple[int, int] = tuple(1, 1),update: bool = False,updateDepthOfField: bool = False,updateLightGlow: bool = False,updateMotionBlur: bool = False,updatePort: str = "",updateShaderGlow: bool = False,updateShading: bool = False,updateShadowMaps: bool = False,useTemplate: str = "") -> None:
    """
    iprEngine を作成、または編集するためのコマンド。iprEngine はシェーディング ネットワークへの変更を監視し、自動的に再シェーディングして、最新のイメージを生成するオブジェクトです。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    copy (string): ディープラスタファイルとこれに関連するファイルを新しい位置にコピーします。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    diagnostics (boolean): 診断が表示されます。

    -----------------------------------------

    estimatedMemory (boolean): IPRで使用されるメモリの見積もり量を表示します。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    iprImage (string): 使用するiprイメージを指定します。

    -----------------------------------------

    motionVectorFile (boolean): IPRで使用されるモーションベクトルファイルの名前を返します。

    -----------------------------------------

    object (name): 調整されるオブジェクトです。

    -----------------------------------------

    region ([int, int, int, int]): 調整する領域の座標です。整数は、左下右上、またはx1y2x2y2の順です。

    -----------------------------------------

    relatedFiles (boolean): 「non-glow-non-blurimage」などの関連ファイル、モーションベクトルファイル、深度マップファイルなどの名前を返します。

    -----------------------------------------

    releaseIprImage (boolean): iprイメージとメモリを解放する必要があります。

    -----------------------------------------

    resolution (boolean): iprファイルの幅と高さです。

    -----------------------------------------

    scanlineIncrement (string): 走査線の増分をパーセントで指定します。更新される領域の高さが240ピクセルでscanlineIncrementが10%の場合、イメージは24走査線を1ブロックとしてリフレッシュされます。

    -----------------------------------------

    showProgressBar (boolean): 調整中に進捗バーを表示します。

    -----------------------------------------

    startTuning (boolean): iprイメージが指定されているときに、シェーディングネットワークを変更して強制的にイメージを生成します。

    -----------------------------------------

    stopTuning (boolean): 調整は終了しますが、iprイメージは閉じられません。

    -----------------------------------------

    underPixel ([int, int]): 指定したピクセル未満のオブジェクトのリストを取得します。

    -----------------------------------------

    update (boolean): 強制更新します。

    -----------------------------------------

    updateDepthOfField (boolean): 被写界深度を強制的にリフレッシュします。

    -----------------------------------------

    updateLightGlow (boolean): ライトグローが変更されたときに自動的に更新します。

    -----------------------------------------

    updateMotionBlur (boolean): 2.5Dモーションブラーが変更されたときに自動的に更新します。

    -----------------------------------------

    updatePort (string): ピクセル値が再計算されたときに更新されるポート番号です(現在は、サポートされていません)。

    -----------------------------------------

    updateShaderGlow (boolean): シェーダグローが変更されたときに自動的に更新します。

    -----------------------------------------

    updateShading (boolean): シェーディングを自動的に更新します。

    -----------------------------------------

    updateShadowMaps (boolean): シャドウマップを強制的に生成、更新します。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    Return Value:
    None: string- 作成または修正された IPR エンジン名照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def layeredShaderPort(annotation: str = "",backgroundColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),defineTemplate: str = "",docTag: str = "",dragCallback: str = "",dropCallback: str = "",enable: bool = False,enableBackground: bool = False,enableKeyboardFocus: bool = False,exists: bool = False,fullPathName: bool = False,height: int = 1,highlightColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),isObscured: bool = False,manage: bool = False,noBackground: bool = False,node: str = "",numberOfPopupMenus: bool = False,parent: str = "",popupMenuArray: bool = False,preventOverride: bool = False,selectedColorControl: str = "",selectedTransparencyControl: str = "",statusBarMessage: str = "",useTemplate: str = "",visible: bool = False,visibleChangeCommand: str = "",width: int = 1) -> None:
    """
    3dPort が作成され、指定した Layered Shader ノードを表すイメージが表示されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    annotation (string): コントロールに文字列値で注釈を付けます。

    -----------------------------------------

    backgroundColor ([float, float, float]): コントロールのバックグラウンドカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。backgroundColorを設定する場合、enableBackgroundをfalseに指定していない限り、バックグラウンドは自動的に有効になります。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    docTag (string): コントロールにドキュメンテーションフラグを追加します。ドキュメンテーションフラグは、ディレクトリ構造になっています。(例:-dtrender/multiLister/createNode/material)

    -----------------------------------------

    dragCallback (script): 中マウスボタンを押すとコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalprocstring[]callbackName(string$dragControl,int$x,int$y,int$mods)procはドロップ先に転送される文字配列を返します。規則により、配列の先頭文字列はユーザ設定可能なメッセージタイプを表しています。アプリケーションで定義されたドラッグ元のコントロールは、このコールバックを無視する可能性があります。$modsで、キーモディファイアであるCTRLとSHIFTをテストできます。有効な値は、0==モディファイアなし、1==SHIFT、2==CTRL、3==CTRL+SHIFTです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defcallbackName(dragControl,x,y,modifiers):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「x」、「y」、「modifiers」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(x)d%(y)d%(modifiers)d'」)。

    -----------------------------------------

    dropCallback (script): ドラッグ＆ドロップ操作をドロップ位置で解放したときにコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalproccallbackName(string$dragControl,string$dropControl,string$msgs[],int$x,int$y,int$type)procは、ドラッグ元から転送される文字配列を受け取ります。msgs配列の先頭文字列はユーザ定義のメッセージタイプを表します。アプリケーションで定義されたドロップ先のコントロールでは、このコールバックが無視されることがあります。$typeの値は、1==移動、2==コピー、3==リンクのいずれかです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defpythonDropTest(dragControl,dropControl,messages,x,y,dragType):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「dropControl」、「messages」、「x」、「y」、「type」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(dropControl)s%(messages)r%(x)d%(y)d%(type)d'」)。

    -----------------------------------------

    enable (boolean): コントロールの有効、無効です。既定ではtrueに設定されていて、コントロールは有効になっています。falseを指定するとコントロールはグレー表示になって無効になります。

    -----------------------------------------

    enableBackground (boolean): コントロールのバックグラウンドカラーを有効にします。

    -----------------------------------------

    enableKeyboardFocus (boolean): 有効にすると、[Tab]キーを押してコントロールに移動し、キーボードまたはマウスで値を選択することができます。このフラグは通常、編集(Edit)コントロールやリスト(List)コントロールなど、既定で表示されるコントロールのフォーカスサポートをオフにする場合に使用します。無効にすると、テキストフィールド内のテキストをマウスで選択することは引き続きできますが、コピーすることはできなくなります(Linuxで[中クリックして貼り付け](MiddleClickPaste)が有効になっている場合は除きます)。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    fullPathName (boolean): すべての親を含むウィジェットのフルパス名を返します。

    -----------------------------------------

    height (int): コントロールの高さです。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    highlightColor ([float, float, float]): コントロールのハイライトカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。

    -----------------------------------------

    isObscured (boolean): コントロールが実際に表示されるかどうかを返します。コントロールは、次の場合に隠れた状態になります。非表示の場合、別のコントロールで(完全に、または部分的に)ブロックされた場合、コントロールまたは親のレイアウトを制御できない場合、あるいはコントロールのウィンドウが非表示またはアイコン化されている場合。

    -----------------------------------------

    manage (boolean): コントロールの状態を管理します。管理されていないコントロールは表示されず、画面の領域も占有しません。既定では、コントロールは管理できるように作成されます。

    -----------------------------------------

    noBackground (boolean): コントロールのバックグラウンドをクリア/リセットします。バックグラウンドは、trueを渡すと一切描画されず、falseを渡すと描画されます。このフラグの状態は、このコントロールの子に継承されます。

    -----------------------------------------

    node (name): このポートが表現するnewLayeredShaderノードの名前を指定します。

    -----------------------------------------

    numberOfPopupMenus (boolean): このコントロールにアタッチされるポップアップメニューの数を返します。

    -----------------------------------------

    parent (string): コントロールの親のレイアウトです。

    -----------------------------------------

    popupMenuArray (boolean): このコントロールにアタッチされる全ポップアップメニューの名前を返します。

    -----------------------------------------

    preventOverride (boolean): trueの場合、コントロールの右マウスボタンメニューを使用したコントロールアトリビュートのオーバーライドは無効になります。

    -----------------------------------------

    selectedColorControl (string): 現在選択されているレイヤのカラーを示すUIコントロールの名前を指定します。

    -----------------------------------------

    selectedTransparencyControl (string): 現在選択しているレイヤの透明度を表すUIコントロールの名前を指定します。

    -----------------------------------------

    statusBarMessage (string): マウスがコントロール上にある場合にステータスバーに表示する追加の文字列です。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    visible (boolean): コントロールの可視の状態です。既定では、コントロールは表示されます。コントロールの実際の外見も、その親レイアウトの可視の状態によって異なることに注意してください。

    -----------------------------------------

    visibleChangeCommand (script): コントロールの可視の状態が変更されたときに実行されるコマンドです。

    -----------------------------------------

    width (int): コントロールの幅を指定します。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    Return Value:
    None: stringコントロールへのフル パス名です。照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def layeredTexturePort(annotation: str = "",backgroundColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),defineTemplate: str = "",docTag: str = "",dragCallback: str = "",dropCallback: str = "",enable: bool = False,enableBackground: bool = False,enableKeyboardFocus: bool = False,exists: bool = False,fullPathName: bool = False,height: int = 1,highlightColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),isObscured: bool = False,manage: bool = False,noBackground: bool = False,node: str = "",numberOfPopupMenus: bool = False,parent: str = "",popupMenuArray: bool = False,preventOverride: bool = False,selectedAlphaControl: str = "",selectedBlendModeControl: str = "",selectedColorControl: str = "",selectedIsVisibleControl: str = "",statusBarMessage: str = "",useTemplate: str = "",visible: bool = False,visibleChangeCommand: str = "",width: int = 1) -> None:
    """
    3dPort が作成され、指定した Layered Texture ノードを表すイメージが表示されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    annotation (string): コントロールに文字列値で注釈を付けます。

    -----------------------------------------

    backgroundColor ([float, float, float]): コントロールのバックグラウンドカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。backgroundColorを設定する場合、enableBackgroundをfalseに指定していない限り、バックグラウンドは自動的に有効になります。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    docTag (string): コントロールにドキュメンテーションフラグを追加します。ドキュメンテーションフラグは、ディレクトリ構造になっています。(例:-dtrender/multiLister/createNode/material)

    -----------------------------------------

    dragCallback (script): 中マウスボタンを押すとコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalprocstring[]callbackName(string$dragControl,int$x,int$y,int$mods)procはドロップ先に転送される文字配列を返します。規則により、配列の先頭文字列はユーザ設定可能なメッセージタイプを表しています。アプリケーションで定義されたドラッグ元のコントロールは、このコールバックを無視する可能性があります。$modsで、キーモディファイアであるCTRLとSHIFTをテストできます。有効な値は、0==モディファイアなし、1==SHIFT、2==CTRL、3==CTRL+SHIFTです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defcallbackName(dragControl,x,y,modifiers):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「x」、「y」、「modifiers」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(x)d%(y)d%(modifiers)d'」)。

    -----------------------------------------

    dropCallback (script): ドラッグ＆ドロップ操作をドロップ位置で解放したときにコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalproccallbackName(string$dragControl,string$dropControl,string$msgs[],int$x,int$y,int$type)procは、ドラッグ元から転送される文字配列を受け取ります。msgs配列の先頭文字列はユーザ定義のメッセージタイプを表します。アプリケーションで定義されたドロップ先のコントロールでは、このコールバックが無視されることがあります。$typeの値は、1==移動、2==コピー、3==リンクのいずれかです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defpythonDropTest(dragControl,dropControl,messages,x,y,dragType):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「dropControl」、「messages」、「x」、「y」、「type」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(dropControl)s%(messages)r%(x)d%(y)d%(type)d'」)。

    -----------------------------------------

    enable (boolean): コントロールの有効、無効です。既定ではtrueに設定されていて、コントロールは有効になっています。falseを指定するとコントロールはグレー表示になって無効になります。

    -----------------------------------------

    enableBackground (boolean): コントロールのバックグラウンドカラーを有効にします。

    -----------------------------------------

    enableKeyboardFocus (boolean): 有効にすると、[Tab]キーを押してコントロールに移動し、キーボードまたはマウスで値を選択することができます。このフラグは通常、編集(Edit)コントロールやリスト(List)コントロールなど、既定で表示されるコントロールのフォーカスサポートをオフにする場合に使用します。無効にすると、テキストフィールド内のテキストをマウスで選択することは引き続きできますが、コピーすることはできなくなります(Linuxで[中クリックして貼り付け](MiddleClickPaste)が有効になっている場合は除きます)。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    fullPathName (boolean): すべての親を含むウィジェットのフルパス名を返します。

    -----------------------------------------

    height (int): コントロールの高さです。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    highlightColor ([float, float, float]): コントロールのハイライトカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。

    -----------------------------------------

    isObscured (boolean): コントロールが実際に表示されるかどうかを返します。コントロールは、次の場合に隠れた状態になります。非表示の場合、別のコントロールで(完全に、または部分的に)ブロックされた場合、コントロールまたは親のレイアウトを制御できない場合、あるいはコントロールのウィンドウが非表示またはアイコン化されている場合。

    -----------------------------------------

    manage (boolean): コントロールの状態を管理します。管理されていないコントロールは表示されず、画面の領域も占有しません。既定では、コントロールは管理できるように作成されます。

    -----------------------------------------

    noBackground (boolean): コントロールのバックグラウンドをクリア/リセットします。バックグラウンドは、trueを渡すと一切描画されず、falseを渡すと描画されます。このフラグの状態は、このコントロールの子に継承されます。

    -----------------------------------------

    node (name): このポートが表現するnewLayeredTextureノードの名前を指定します。

    -----------------------------------------

    numberOfPopupMenus (boolean): このコントロールにアタッチされるポップアップメニューの数を返します。

    -----------------------------------------

    parent (string): コントロールの親のレイアウトです。

    -----------------------------------------

    popupMenuArray (boolean): このコントロールにアタッチされる全ポップアップメニューの名前を返します。

    -----------------------------------------

    preventOverride (boolean): trueの場合、コントロールの右マウスボタンメニューを使用したコントロールアトリビュートのオーバーライドは無効になります。

    -----------------------------------------

    selectedAlphaControl (string): 現在選択しているレイヤのアルファを表すUIコントロールの名前を指定します。

    -----------------------------------------

    selectedBlendModeControl (string): 現在選択しているレイヤのブレンドモードを表すUIコントロールの名前を指定します。

    -----------------------------------------

    selectedColorControl (string): 現在選択されているレイヤのカラーを示すUIコントロールの名前を指定します。

    -----------------------------------------

    selectedIsVisibleControl (string): 現在選択しているレイヤの可視性を表すUIコントロールの名前を指定します。

    -----------------------------------------

    statusBarMessage (string): マウスがコントロール上にある場合にステータスバーに表示する追加の文字列です。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    visible (boolean): コントロールの可視の状態です。既定では、コントロールは表示されます。コントロールの実際の外見も、その親レイアウトの可視の状態によって異なることに注意してください。

    -----------------------------------------

    visibleChangeCommand (script): コントロールの可視の状態が変更されたときに実行されるコマンドです。

    -----------------------------------------

    width (int): コントロールの幅を指定します。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    Return Value:
    None: stringコントロールへのフル パス名です。照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def lsThroughFilter(item: str = "",nodeArray: bool = False,reverse: bool = False,selection: bool = False,sort: str = "") -> None:
    """
    特定フィルタを通過した、ワールド内のすべてのオブジェクトがリストされます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    item (string): このコマンドの高速バージョンを使用して、指定したノードにフィルタを実行します。

    -----------------------------------------

    nodeArray (boolean): フィルタを通してノード配列全体を同時に実行する高速バージョンです。

    -----------------------------------------

    reverse (boolean): nodeArrayフラグと一緒にのみ使用可能です。trueの場合、返される配列内のノードの順序を逆にします。

    -----------------------------------------

    selection (boolean): このコマンドの高速バージョンを使用して、選択したノードのみにフィルタを実行します。

    -----------------------------------------

    sort (string): nodeArrayフラグと一緒にのみ使用可能です。返される配列内のノードを順序付けします。現在のオプションは、「byName」、「byType」、および「byTime」です。

    -----------------------------------------

    Return Value:
    None: string[]フィルタを通過するノードのリスト
    """
    pass

    
def makebot(checkdepends: bool = False,checkres: int = 1,input: str = "",nooverwrite: bool = False,output: str = "",verbose: bool = False) -> None:
    """
    イメージ ファイルを取り、BOT (ブロック順序テクスチャ)ファイルを作成してテクスチャ キャッシュに使用します。入力イメージ ファイルとして相対パス名を指定すると、プロジェクト管理ルールが適用されます。出力 BOT ファイルとして相対パス名を指定すると、プロジェクト管理ルールが適用されて sourceImages ディレクトリに配置されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    checkdepends (boolean): BOTファイルがまだないか、またはソースファイルより古い場合にのみ、生成されます。

    -----------------------------------------

    checkres (uint): BOTファイルの解像度(幅と高さの最大値)が引数で指定した最低値よりも大きい場合にのみ、生成されます。

    -----------------------------------------

    input (string): 入力イメージファイル

    -----------------------------------------

    nooverwrite (boolean): -cや-rでBOTファイルを生成するよう指定したがすでにファイルが存在していた場合に、このフラグを使うと、ファイルが上書きされないようにすることができます。

    -----------------------------------------

    output (string): 出力BOTファイル

    -----------------------------------------

    verbose (boolean): このフラグが指定されていると、Makebotからフィードバックが得られます。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def mayaHasRenderSetup(enableCurrentSession: bool = False,enableDuringTests: bool = False) -> None:
    """
    このコマンドは、レンダリングの設定状態をコントロールおよび照会します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    enableCurrentSession (boolean): このMayaセッションのレンダリング設定のみを有効または無効にします。このフラグは、Mayaの初期化中のみ呼び出す必要があります。このフラグは、内部専用です。任意の時点で変更される可能性があるため、サポートされていません。

    -----------------------------------------

    enableDuringTests (boolean): テスト中は旧式のレンダーレイヤモードが使用されるため、このMayaセッションのレンダリング設定のみを切り替えます。このフラグは、内部専用です。任意の時点で変更される可能性があるため、サポートされていません。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def nodeIconButton(align: str = "",annotation: str = "",backgroundColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),command: str = "",defineTemplate: str = "",disabledImage: str = "",docTag: str = "",dragCallback: str = "",dropCallback: str = "",enable: bool = False,enableBackground: bool = False,enableKeyboardFocus: bool = False,exists: bool = False,flipX: bool = False,flipY: bool = False,font: str = "",fullPathName: bool = False,height: int = 1,highlightColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),image: str = "",image1: str = "",image2: str = "",image3: str = "",imageOverlayLabel: str = "",isObscured: bool = False,label: str = "",labelOffset: int = 1,ltVersion: str = "",manage: bool = False,marginHeight: int = 1,marginWidth: int = 1,noBackground: bool = False,numberOfPopupMenus: bool = False,overlayLabelBackColor: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),overlayLabelColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),parent: str = "",popupMenuArray: bool = False,preventOverride: bool = False,rotation: float = 1.0,statusBarMessage: str = "",style: str = "",useAlpha: bool = False,useTemplate: str = "",version: str = "",visible: bool = False,visibleChangeCommand: str = "",width: int = 1) -> None:
    """
    このコントロールは、アイコン イメージを最大 3 つまで、ディスプレイ スタイルを最大 4 つまでサポートします。現在のスタイルが指定されている場合、表示されるアイコン イメージは、コントロールの現在のサイズに最適なイメージです。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    align (string): ラベル位置合わせです。位置合わせの値は、「left」、「right」、「center」です。既定では、ラベルは「center」に位置合わせます。現在は、-st/styleが「iconAndTextCentered」に設定されている場合にのみ使用可能です。

    -----------------------------------------

    annotation (string): コントロールに文字列値で注釈を付けます。

    -----------------------------------------

    backgroundColor ([float, float, float]): コントロールのバックグラウンドカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。backgroundColorを設定する場合、enableBackgroundをfalseに指定していない限り、バックグラウンドは自動的に有効になります。

    -----------------------------------------

    command (script): コントロールを押したときに実行されるコマンドです。このコマンドは、ノードのドラッグ＆ドロップを可能にする文字列を返します。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    disabledImage (string): ボタンが無効になっているときに使用されるイメージです。イメージのサイズは、-i/imageフラグで指定したイメージのサイズと同じである必要があります。これはWindows専用のフラグです。

    -----------------------------------------

    docTag (string): コントロールにドキュメンテーションフラグを追加します。ドキュメンテーションフラグは、ディレクトリ構造になっています。(例:-dtrender/multiLister/createNode/material)

    -----------------------------------------

    dragCallback (script): 中マウスボタンを押すとコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalprocstring[]callbackName(string$dragControl,int$x,int$y,int$mods)procはドロップ先に転送される文字配列を返します。規則により、配列の先頭文字列はユーザ設定可能なメッセージタイプを表しています。アプリケーションで定義されたドラッグ元のコントロールは、このコールバックを無視する可能性があります。$modsで、キーモディファイアであるCTRLとSHIFTをテストできます。有効な値は、0==モディファイアなし、1==SHIFT、2==CTRL、3==CTRL+SHIFTです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defcallbackName(dragControl,x,y,modifiers):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「x」、「y」、「modifiers」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(x)d%(y)d%(modifiers)d'」)。

    -----------------------------------------

    dropCallback (script): ドラッグ＆ドロップ操作をドロップ位置で解放したときにコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalproccallbackName(string$dragControl,string$dropControl,string$msgs[],int$x,int$y,int$type)procは、ドラッグ元から転送される文字配列を受け取ります。msgs配列の先頭文字列はユーザ定義のメッセージタイプを表します。アプリケーションで定義されたドロップ先のコントロールでは、このコールバックが無視されることがあります。$typeの値は、1==移動、2==コピー、3==リンクのいずれかです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defpythonDropTest(dragControl,dropControl,messages,x,y,dragType):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「dropControl」、「messages」、「x」、「y」、「type」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(dropControl)s%(messages)r%(x)d%(y)d%(type)d'」)。

    -----------------------------------------

    enable (boolean): コントロールの有効、無効です。既定ではtrueに設定されていて、コントロールは有効になっています。falseを指定するとコントロールはグレー表示になって無効になります。

    -----------------------------------------

    enableBackground (boolean): コントロールのバックグラウンドカラーを有効にします。

    -----------------------------------------

    enableKeyboardFocus (boolean): 有効にすると、[Tab]キーを押してコントロールに移動し、キーボードまたはマウスで値を選択することができます。このフラグは通常、編集(Edit)コントロールやリスト(List)コントロールなど、既定で表示されるコントロールのフォーカスサポートをオフにする場合に使用します。無効にすると、テキストフィールド内のテキストをマウスで選択することは引き続きできますが、コピーすることはできなくなります(Linuxで[中クリックして貼り付け](MiddleClickPaste)が有効になっている場合は除きます)。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    flipX (boolean): イメージを水平方向に反転するかどうかを指定します。

    -----------------------------------------

    flipY (boolean): イメージを垂直方向に反転するかどうかを指定します。

    -----------------------------------------

    font (string): テキストのフォントです。有効な値は、「boldLabelFont」、「smallBoldLabelFont」、「tinyBoldLabelFont」、「plainLabelFont」、「smallPlainLabelFont」、「obliqueLabelFont」、「smallObliqueLabelFont」、「fixedWidthFont」、「smallFixedWidthFont」です。

    -----------------------------------------

    fullPathName (boolean): すべての親を含むウィジェットのフルパス名を返します。

    -----------------------------------------

    height (int): コントロールの高さです。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    highlightColor ([float, float, float]): コントロールのハイライトカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。

    -----------------------------------------

    image (string): サイズの異なるイメージがなければ、このフラグをコントロールのイメージに使用できます。「iconOnly」スタイルを設定すると、アイコンはコントロールのサイズに合わせてスケーリングされます。

    -----------------------------------------

    image1 (string): 3つの可能なアイコンの中の1番目です。コントロールの現在のサイズに最適なアイコンが表示されます。

    -----------------------------------------

    image2 (string): 3つの可能なアイコンの中の2番目です。コントロールの現在のサイズに最適なアイコンが表示されます。

    -----------------------------------------

    image3 (string): 3つの可能なアイコンの中の3番目です。コントロールの現在のサイズに最適なアイコンが表示されます。

    -----------------------------------------

    imageOverlayLabel (string): イメージ上に表示されるラベルを表す、最大6文字の短い文字列です。

    -----------------------------------------

    isObscured (boolean): コントロールが実際に表示されるかどうかを返します。コントロールは、次の場合に隠れた状態になります。非表示の場合、別のコントロールで(完全に、または部分的に)ブロックされた場合、コントロールまたは親のレイアウトを制御できない場合、あるいはコントロールのウィンドウが非表示またはアイコン化されている場合。

    -----------------------------------------

    label (string): コントロールに表示されるテキストです。

    -----------------------------------------

    labelOffset (int): ラベルオフセットです。既定は0です。現在は、-st/styleが「iconAndTextCentered」に設定されている場合にのみ使用可能です。

    -----------------------------------------

    ltVersion (string): このフラグは、バージョンフラグが指定されない場合、またはバージョンフラグは指定されているが引数が異なる場合に、このコントロール機能が導入されているMayaLTバージョンを指定するために使用されます。この値はMayaLTのみで使用され、それ以外では無視されます。引数は、バージョン番号の文字列として指定する必要があります(例:「2013」、「2014」)。現時点では、メジャーバージョン番号のみが受け入れられます(例:2013Ext1または2013.5は「2014」と指定する必要があります)。

    -----------------------------------------

    manage (boolean): コントロールの状態を管理します。管理されていないコントロールは表示されず、画面の領域も占有しません。既定では、コントロールは管理できるように作成されます。

    -----------------------------------------

    marginHeight (uint): コントロールコンテンツの上下にあるピクセル数。既定値は1ピクセルです。

    -----------------------------------------

    marginWidth (uint): コントロールコンテンツの両側にあるピクセル数。既定値は1ピクセルです。

    -----------------------------------------

    noBackground (boolean): コントロールのバックグラウンドをクリア/リセットします。バックグラウンドは、trueを渡すと一切描画されず、falseを渡すと描画されます。このフラグの状態は、このコントロールの子に継承されます。

    -----------------------------------------

    numberOfPopupMenus (boolean): このコントロールにアタッチされるポップアップメニューの数を返します。

    -----------------------------------------

    overlayLabelBackColor ([float, float, float, float]): imageOverlayLabelが定義するラベルの影のRGBAカラーです。既定は透過率50%の黒です:000.5

    -----------------------------------------

    overlayLabelColor ([float, float, float]): imageOverlayLabelが定義するラベルのRGBカラーです。既定は薄いグレーです:.8.8.8

    -----------------------------------------

    parent (string): コントロールの親のレイアウトです。

    -----------------------------------------

    popupMenuArray (boolean): このコントロールにアタッチされる全ポップアップメニューの名前を返します。

    -----------------------------------------

    preventOverride (boolean): trueの場合、コントロールの右マウスボタンメニューを使用したコントロールアトリビュートのオーバーライドは無効になります。

    -----------------------------------------

    rotation (float): イメージの回転値(ラジアン)です。

    -----------------------------------------

    statusBarMessage (string): マウスがコントロール上にある場合にステータスバーに表示する追加の文字列です。

    -----------------------------------------

    style (string): コントロールの描画スタイルです。有効なスタイルは、「iconOnly」、「textOnly」、「iconAndTextHorizontal」、「iconAndTextVertical」と「iconAndTextCentered」です(注:「iconAndTextCentered」はWindowsのみで使用可能です)。「iconOnly」スタイルを設定すると、アイコンはコントロールのサイズに合わせてスケーリングされます。

    -----------------------------------------

    useAlpha (boolean): イメージにアルファチャネルを使用するかどうかを指定します。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    version (string): このコントロール機能が導入されたバージョンを指定します。引数は、バージョン番号の文字列として指定する必要があります(例:「2013」、「2014」)。現時点では、メジャーバージョン番号のみが受け入れられます(例:2013Ext1または2013.5は「2014」と指定する必要があります)。

    -----------------------------------------

    visible (boolean): コントロールの可視の状態です。既定では、コントロールは表示されます。コントロールの実際の外見も、その親レイアウトの可視の状態によって異なることに注意してください。

    -----------------------------------------

    visibleChangeCommand (script): コントロールの可視の状態が変更されたときに実行されるコマンドです。

    -----------------------------------------

    width (int): コントロールの幅を指定します。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    Return Value:
    None: stringボタンの名前照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def nodePreset(attributes: str = "",custom: str = "",delete: Tuple[str, str] = tuple("", ""),exists: Tuple[str, str] = tuple("", ""),isValidName: str = "",list: str = "",load: Tuple[str, str] = tuple("", ""),save: Tuple[str, str] = tuple("", "")) -> None:
    """
    ノードのプリセットの設定を保存/ロードするためのコマンドです。このコマンドで、ノードのすべてのアトリビュート値を記録し、任意の名前を付けてディスクに保存することができます。保存したプリセットをロードし、同じタイプのノードに適用することができます。プリセットを適用したノードの値は、プリセットを生成したノードの、記録した時点での値と同じになります。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    attributes (string): プリセットファイルに保存する指定アトリビュートの、空白で区切られた文字列です。指定していない場合、すべてのアトリビュートが格納されます。

    -----------------------------------------

    custom (string): マルチ、ダイナミックアトリビュート、接続などの一般的なプリセットの保存の仕組みによって処理されないノードアトリビュートをカスタムで処理するためのMELスクリプトを指定します。#presetNameと#nodeNameの識別子は、スクリプトの実行前に展開されます。このスクリプトは、プリセットファイルに保存され、プリセットを別のノードに適用した際に、これをコマンドとして実行する文字配列を返す必要があります。このカスタムスクリプトを使用して、プリセットへの保存内容を定義する#nodeNameの照会や、プリセットの適用方法を定義するために、選択したノードを照会するコマンドの実行ができます。

    -----------------------------------------

    delete ([name, string]): 2番目の引数で指定した名前を持つ、1番目の引数で指定したノードのプリセットを削除します。

    -----------------------------------------

    exists ([name, string]): 1番目の引数で指定したノードに2番目の引数で指定した名前のプリセットが存在する場合、trueを返します。このフラグを使用して、既存のプリセットが上書きされてしまうかどうかを確認でき、上書きしたくない場合は別の名前を付けることができます。

    -----------------------------------------

    isValidName (string): プリセット名を構成する文字がすべて有効であればtrueを返します。それ以外の場合にはfalseを返します。プリセット名はファイル名やMELプロシージャ名の一部になるため、無効な文字も設定されています。プリセット名の有効文字は、英数字とアンダースコアのみです。

    -----------------------------------------

    list (name): 指定したノードにロードすることができるすべてのプリセット名をリスト表示します。

    -----------------------------------------

    load ([name, string]): 1番目の引数で指定したノードの設定を、2番目の引数で指定したプリセットに従って設定します。接続先のノード、あるいはその子(複数の子、あるいは合成された子)は、このプリセットでは変更されません。

    -----------------------------------------

    save ([name, string]): 1番目の引数で指定したノードの現在の設定を、2番目の引数で指定した名前のプリセットに保存します。指定した名前のプリセットがノードに存在する場合、警告メッセージを出すことなく上書きします。-existsフラグを使用して、該当プリセットが存在しているかどうかを確認できます。ノードのアトリビュートが接続先の場合は、そのアトリビュート値はプリセットとして書き込まれません。

    -----------------------------------------

    Return Value:
    None: booleanisValidName または exists が使用されているかどうか。
    """
    pass

    
def ogsRender(activeMultisampleType: str = "",activeRenderOverride: str = "",activeRenderTargetFormat: str = "",availableFloatingPointTargetFormat: bool = False,availableMultisampleType: bool = False,availableRenderOverrides: bool = False,camera: str = "",currentFrame: bool = False,currentView: bool = False,enableFloatingPointRenderTarget: bool = False,enableMultisample: bool = False,frame: float = 1.0,height: int = 1,layer: str = "",noRenderView: bool = False,width: int = 1) -> None:
    """
    OGS レンダリング エンジンを使用してイメージまたはシーケンスをレンダーします。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    activeMultisampleType (string): 現在のアクティブなマルチサンプルタイプを照会します。

    -----------------------------------------

    activeRenderOverride (string): 現在のアクティブなレンダーオーバーライドを設定または照会します。

    -----------------------------------------

    activeRenderTargetFormat (string): 現在のアクティブな浮動小数ターゲットフォーマットを照会します。

    -----------------------------------------

    availableFloatingPointTargetFormat (boolean): 使用可能な浮動小数レンダーターゲットフォーマットの名前を返します。

    -----------------------------------------

    availableMultisampleType (boolean): 使用可能なマルチサンプルタイプを返します。

    -----------------------------------------

    availableRenderOverrides (boolean): 使用可能なレンダーオーバーライドの名前を返します。

    -----------------------------------------

    camera (string): 使用するカメラを指定します。指定のカメラが見つからない場合は、使用可能な最初のカメラを使用します。

    -----------------------------------------

    currentFrame (boolean): 現在のフレームをレンダーします。

    -----------------------------------------

    currentView (boolean): オンにすると、現在選択しているビューのみがレンダーされます。

    -----------------------------------------

    enableFloatingPointRenderTarget (boolean): 浮動小数レンダーターゲットを有効化/無効化します。

    -----------------------------------------

    enableMultisample (boolean): マルチサンプルを有効化/無効化します。

    -----------------------------------------

    frame (float): レンダーするフレームを指定します。

    -----------------------------------------

    height (uint): heightフラグは、指定した高さをogsRenderコマンドに渡します。このフラグを使用しない場合、高さはレンダーグローバル(RenderGlobals)設定から取得されます。

    -----------------------------------------

    layer (name): 指定したレンダーレイヤをレンダーします。レンダーレイヤのレンダリング可能なアトリビュート値にかかわらず、このレンダーレイヤのみをレンダーします。レイヤ名は出力イメージファイル名にアペンドされます。指定したレンダーレイヤは、レンダリング前に現在のレンダーレイヤになり、レンダリング後も現在のレンダーレイヤのままです。

    -----------------------------------------

    noRenderView (boolean): オンにすると、イメージの計算後にレンダービューが更新されません。

    -----------------------------------------

    width (uint): widthフラグは、指定した幅をogsRenderコマンドに渡します。このフラグを使用しない場合、幅はレンダーグローバル(RenderGlobals)設定から取得されます。

    -----------------------------------------

    Return Value:
    None: boolean照会結果照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def preferredRenderer(fallback: str = "",makeCurrent: bool = False) -> None:
    """
    優先レンダラを設定するコマンドです。このコマンドは、優先レンダラを検索したり、現在のレンダラを優先レンダラの 1 つとして設定する場合に使用できます。優先フォールバック レンダラを指定することもできます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    fallback (string): 優先フォールバックレンダラを設定します。

    -----------------------------------------

    makeCurrent (boolean): 現在のレンダラが優先レンダラになるように設定します。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def prepareRender(defaultTraversalSet: str = "",deregister: str = "",invokePostRender: bool = False,invokePostRenderFrame: bool = False,invokePostRenderLayer: bool = False,invokePreRender: bool = False,invokePreRenderFrame: bool = False,invokePreRenderLayer: bool = False,invokeSettingsUI: bool = False,label: str = "",listTraversalSets: bool = False,postRender: str = "",postRenderFrame: str = "",postRenderLayer: str = "",preRender: str = "",preRenderFrame: str = "",preRenderLayer: str = "",restore: bool = False,saveAssemblyConfig: bool = False,settingsUI: str = "",setup: bool = False,traversalSet: str = "",traversalSetInit: str = "") -> None:
    """
    このコマンドは、レンダー縦断を登録、管理および呼び出すために使用されます。レンダー縦断は、シーンを構成してレンダリングの準備をするために使用されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    defaultTraversalSet (string): 既定の縦断セットを設定または照会します。prepareRenderコマンドは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セット上で操作を実行します。

    -----------------------------------------

    deregister (string): 登録された縦断セットを登録解除します。登録解除された縦断セットが既定の縦断セットの場合、新しい既定の縦断セットは「null」縦断セットになります。

    -----------------------------------------

    invokePostRender (boolean): 特定の縦断セットに対するpostRenderレンダー縦断を呼び出します。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    invokePostRenderFrame (boolean): 特定の縦断セットに対するpostRenderFrameレンダー縦断を呼び出します。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    invokePostRenderLayer (boolean): 特定の縦断セットに対するpostRenderLayerレンダー縦断を呼び出します。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    invokePreRender (boolean): 特定の縦断セットに対するpreRenderレンダー縦断を呼び出します。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    invokePreRenderFrame (boolean): 特定の縦断セットに対するpreRenderFrameレンダー縦断を呼び出します。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    invokePreRenderLayer (boolean): 特定の縦断セットに対するpreRenderLayerレンダー縦断を呼び出します。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    invokeSettingsUI (boolean): 特定の縦断セットに対する、設定UIコールバックを呼び出してレイアウトにUIコントロールを設定します。現在のUIの親はフォームレイアウトであり、コールバックはsetParentコマンドを使用してクエリを実行できます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    label (string): 特定の縦断セットのラベルを設定または照会します。ラベルはUI表示の目的で使用され、ローカライズできます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定になります。

    -----------------------------------------

    listTraversalSets (boolean): サポートされているレンダー縦断セットを照会します。

    -----------------------------------------

    postRender (script): 特定の縦断セットに対するpostRenderレンダー縦断を設定または照会します。この縦断はレンダー後に実行されます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    postRenderFrame (script): 特定の縦断セットに対するpostRenderFrameレンダー縦断を設定または照会します。この縦断は、レンダーレイヤを持つ単一フレームのレンダーの後に実行されます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    postRenderLayer (script): 特定の縦断セットに対するpostRenderLayerレンダー縦断を設定または照会します。この縦断はレンダーレイヤがレンダリグされた後に、レンダー内で実行されます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    preRender (script): 特定の縦断セットに対するpreRenderレンダー縦断を設定または照会します。この縦断はレンダー前に実行されます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    preRenderFrame (script): 特定の縦断セットに対するpreRenderFrameレンダー縦断を設定または照会します。この縦断は、レンダーレイヤを持つ単一フレームのレンダーの前に実行されます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    preRenderLayer (script): 特定の縦断セットに対するpreRenderLayerレンダー縦断を設定または照会します。この縦断はレンダーレイヤがレンダリグされる前に、レンダー内で実行されます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    restore (boolean): 縦断のsaveAssemblyConfigフラグがtrueに設定されている場合、レンダリングをクリーンアップします。これにはシーン全体のアセンブリアクティブリプリゼンテーション設定の復元が含まれます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    saveAssemblyConfig (boolean): シーン全体のアクティブリプリゼンテーション設定を特定の縦断セットに対して保存するかどうかを設定または照会します。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定になります。

    -----------------------------------------

    settingsUI (script): 特定の縦断セットに対する設定UIコールバックを設定または照会します。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    setup (boolean): 縦断のsaveAssemblyConfigフラグがtrueに設定されている場合、レンダー準備を設定します。これにはシーン全体のアセンブリアクティブリプリゼンテーション設定の保存が含まれます。以前に保存された設定は上書きされます。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。

    -----------------------------------------

    traversalSet (string): 指定した登録済み縦断セットのプロパティを設定または照会します。照会モードでは、このフラグに値が必要になります。

    -----------------------------------------

    traversalSetInit (script): 特定の走査セットに対する走査セット初期化コールバックを設定または照会します。縦断セットは、-traversalSetフラグを使用して縦断セットを明示的に指定しない限り、既定の縦断セットになります。このコールバックは、指定された走査セットが既定の走査セットになるたびに呼び出されます。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def projectionManip(fitBBox: bool = False,projType: int = 1,switchType: bool = False) -> None:
    """
    マニピュレータを、任意の位置に設定するための各種コマンドです。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    fitBBox (boolean): 投影マニピュレータのサイズと位置を、シェーディンググループバウンディングボックスに合わせます。方向は変更されません。

    -----------------------------------------

    projType (int): 投影タイプを指定した値に設定します。投影タイプの値は次のとおりです。1=平面。2=球面。3=円柱。4=球。5=三次。6=トライプレーン。7=同心。8=カメラ。

    -----------------------------------------

    switchType (boolean): 使用できるタイプをループします。ハードウェアシェーディングがオンの場合、ハードウェアシェーディングできるタイプ(planar、cylindrical、spherical)をループします。それ以外の場合は、すべてのタイプをループします。値が指定されていない場合、異なる投影タイプをループします。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def rampColorPort(annotation: str = "",backgroundColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),defineTemplate: str = "",docTag: str = "",dragCallback: str = "",dropCallback: str = "",enable: bool = False,enableBackground: bool = False,enableKeyboardFocus: bool = False,exists: bool = False,fullPathName: bool = False,height: int = 1,highlightColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),isObscured: bool = False,manage: bool = False,noBackground: bool = False,node: str = "",numberOfPopupMenus: bool = False,parent: str = "",popupMenuArray: bool = False,preventOverride: bool = False,selectedColorControl: str = "",selectedInterpControl: str = "",selectedPositionControl: str = "",statusBarMessage: str = "",useTemplate: str = "",verticalLayout: bool = False,visible: bool = False,visibleChangeCommand: str = "",width: int = 1) -> None:
    """
    このコマンドは指定した Ramp ノードを表すイメージを表示するコントロールを作成し、そのノードの編集をサポートします。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    annotation (string): コントロールに文字列値で注釈を付けます。

    -----------------------------------------

    backgroundColor ([float, float, float]): コントロールのバックグラウンドカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。backgroundColorを設定する場合、enableBackgroundをfalseに指定していない限り、バックグラウンドは自動的に有効になります。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    docTag (string): コントロールにドキュメンテーションフラグを追加します。ドキュメンテーションフラグは、ディレクトリ構造になっています。(例:-dtrender/multiLister/createNode/material)

    -----------------------------------------

    dragCallback (script): 中マウスボタンを押すとコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalprocstring[]callbackName(string$dragControl,int$x,int$y,int$mods)procはドロップ先に転送される文字配列を返します。規則により、配列の先頭文字列はユーザ設定可能なメッセージタイプを表しています。アプリケーションで定義されたドラッグ元のコントロールは、このコールバックを無視する可能性があります。$modsで、キーモディファイアであるCTRLとSHIFTをテストできます。有効な値は、0==モディファイアなし、1==SHIFT、2==CTRL、3==CTRL+SHIFTです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defcallbackName(dragControl,x,y,modifiers):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「x」、「y」、「modifiers」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(x)d%(y)d%(modifiers)d'」)。

    -----------------------------------------

    dropCallback (script): ドラッグ＆ドロップ操作をドロップ位置で解放したときにコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalproccallbackName(string$dragControl,string$dropControl,string$msgs[],int$x,int$y,int$type)procは、ドラッグ元から転送される文字配列を受け取ります。msgs配列の先頭文字列はユーザ定義のメッセージタイプを表します。アプリケーションで定義されたドロップ先のコントロールでは、このコールバックが無視されることがあります。$typeの値は、1==移動、2==コピー、3==リンクのいずれかです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defpythonDropTest(dragControl,dropControl,messages,x,y,dragType):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「dropControl」、「messages」、「x」、「y」、「type」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(dropControl)s%(messages)r%(x)d%(y)d%(type)d'」)。

    -----------------------------------------

    enable (boolean): コントロールの有効、無効です。既定ではtrueに設定されていて、コントロールは有効になっています。falseを指定するとコントロールはグレー表示になって無効になります。

    -----------------------------------------

    enableBackground (boolean): コントロールのバックグラウンドカラーを有効にします。

    -----------------------------------------

    enableKeyboardFocus (boolean): 有効にすると、[Tab]キーを押してコントロールに移動し、キーボードまたはマウスで値を選択することができます。このフラグは通常、編集(Edit)コントロールやリスト(List)コントロールなど、既定で表示されるコントロールのフォーカスサポートをオフにする場合に使用します。無効にすると、テキストフィールド内のテキストをマウスで選択することは引き続きできますが、コピーすることはできなくなります(Linuxで[中クリックして貼り付け](MiddleClickPaste)が有効になっている場合は除きます)。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    fullPathName (boolean): すべての親を含むウィジェットのフルパス名を返します。

    -----------------------------------------

    height (int): コントロールの高さです。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    highlightColor ([float, float, float]): コントロールのハイライトカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。

    -----------------------------------------

    isObscured (boolean): コントロールが実際に表示されるかどうかを返します。コントロールは、次の場合に隠れた状態になります。非表示の場合、別のコントロールで(完全に、または部分的に)ブロックされた場合、コントロールまたは親のレイアウトを制御できない場合、あるいはコントロールのウィンドウが非表示またはアイコン化されている場合。

    -----------------------------------------

    manage (boolean): コントロールの状態を管理します。管理されていないコントロールは表示されず、画面の領域も占有しません。既定では、コントロールは管理できるように作成されます。

    -----------------------------------------

    noBackground (boolean): コントロールのバックグラウンドをクリア/リセットします。バックグラウンドは、trueを渡すと一切描画されず、falseを渡すと描画されます。このフラグの状態は、このコントロールの子に継承されます。

    -----------------------------------------

    node (name): このポートが表すnewRampテクスチャノードの名前を指定します。

    -----------------------------------------

    numberOfPopupMenus (boolean): このコントロールにアタッチされるポップアップメニューの数を返します。

    -----------------------------------------

    parent (string): コントロールの親のレイアウトです。

    -----------------------------------------

    popupMenuArray (boolean): このコントロールにアタッチされる全ポップアップメニューの名前を返します。

    -----------------------------------------

    preventOverride (boolean): trueの場合、コントロールの右マウスボタンメニューを使用したコントロールアトリビュートのオーバーライドは無効になります。

    -----------------------------------------

    selectedColorControl (string): もしあれば、ランプで現在選択されているエントリのカラーを表示するコントロールの名前を設定します。このコントロールは、ユーザがランプで異なるエントリを選択したときに自動的に更新され、編集すると選択したエントリは修正されます。コントロールのタイプはattrColorSliderGrpでなければなりません。

    -----------------------------------------

    selectedInterpControl (string): もしあれば、ランプで現在選択されているエントリの補間を表示するコントロールの名前を設定します。このコントロールは、ユーザがランプで異なるエントリを選択したときに自動的に更新され、編集すると選択したエントリは修正されます。コントロールのタイプはattrEnumOptionMenuGrpでなければなりません。

    -----------------------------------------

    selectedPositionControl (string): もしあれば、ランプで現在選択されているエントリの位置を表示するコントロールの名前を設定します。このコントロールは、ユーザがランプで異なるエントリを選択したときに自動的に更新され、編集すると選択したエントリは修正されます。コントロールのタイプはattrFieldSliderGrpでなければなりません。

    -----------------------------------------

    statusBarMessage (string): マウスがコントロール上にある場合にステータスバーに表示する追加の文字列です。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    verticalLayout (boolean): プレビューのレイアウトを設定します。

    -----------------------------------------

    visible (boolean): コントロールの可視の状態です。既定では、コントロールは表示されます。コントロールの実際の外見も、その親レイアウトの可視の状態によって異なることに注意してください。

    -----------------------------------------

    visibleChangeCommand (script): コントロールの可視の状態が変更されたときに実行されるコマンドです。

    -----------------------------------------

    width (int): コントロールの幅を指定します。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    Return Value:
    None: string作成または修正されたポート名照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def render(abortMissingTexture: bool = False,batch: bool = False,keepPreImage: bool = False,layer: str = "",nglowpass: bool = False,nshadows: bool = False,replace: bool = False,xresolution: int = 1,yresolution: int = 1) -> None:
    """
    render コマンドは、現在アクティブになっているカメラの MayaSoftware レンダリング セッションを開始するために使用されます。レンダリングがすでに実行中であれば、このコマンドはレンダリングを中止します。このコマンドは元に戻せません。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    abortMissingTexture (boolean): 欠落しているテクスチャがあるとレンダラが異常終了します。-batchが設定されている場合のみ使用可能です。

    -----------------------------------------

    batch (boolean): バッチモードで実行します。レンダリング可能なすべてのカメラのイメージを計算します。このMELのフラグは、-renderフラグを設定してバッチモードでMayaを実行するのと同等の機能を持ちます。-batchを使用すると、他のすべてのフラグは無視されます。

    -----------------------------------------

    keepPreImage (boolean): 後処理より前にレンダリングを維持します。-batchが設定されている場合のみ使用可能です。

    -----------------------------------------

    layer (string): 指定したレンダーレイヤをレンダーします。レンダーレイヤのレンダリング可能なアトリビュート値にかかわらず、このレンダーレイヤのみをレンダーします。レイヤ名は出力イメージファイル名にアペンドされます。指定したレンダーレイヤは、レンダリング前に現在のレンダーレイヤになり、レンダリング後も現在のレンダーレイヤのままです。

    -----------------------------------------

    nglowpass (boolean): グローパス機能を上書きします(この値をfalseに設定すると、グローパスをグローバルでオフにできます)。

    -----------------------------------------

    nshadows (boolean): シャドウ機能を上書きします(この値をfalseに設定すると、シャドウをグローバルでオフにできます)。

    -----------------------------------------

    replace (boolean): レンダリングイメージがすでに存在する場合にこれを置き換えます。-batchが設定されている場合のみ使用可能です。

    -----------------------------------------

    xresolution (int): x解像度を上書きします。

    -----------------------------------------

    yresolution (int): y解像度を上書きします。

    -----------------------------------------

    Return Value:
    None: stringレンダリング イメージの名前。
    """
    pass

    
def renderer(addGlobalsNode: str = "",addGlobalsTab: Tuple[str, str, str] = tuple("", "", ""),batchRenderOptionsProcedure: str = "",batchRenderOptionsStringProcedure: str = "",batchRenderProcedure: str = "",cancelBatchRenderProcedure: str = "",changeIprRegionProcedure: str = "",commandRenderProcedure: str = "",exists: bool = False,globalsNodes: bool = False,globalsTabCreateProcNames: bool = False,globalsTabLabels: bool = False,globalsTabUpdateProcNames: bool = False,iprOptionsMenuLabel: str = "",iprOptionsProcedure: str = "",iprOptionsSubMenuProcedure: str = "",iprRenderProcedure: str = "",iprRenderSubMenuProcedure: str = "",isRunningIprProcedure: str = "",logoCallbackProcedure: str = "",logoImageName: str = "",materialViewRendererList: bool = False,materialViewRendererPause: bool = False,materialViewRendererSuspend: bool = False,namesOfAvailableRenderers: bool = False,pauseIprRenderProcedure: str = "",polyPrelightProcedure: str = "",refreshIprRenderProcedure: str = "",renderDiagnosticsProcedure: str = "",renderGlobalsProcedure: str = "",renderMenuProcedure: str = "",renderOptionsProcedure: str = "",renderProcedure: str = "",renderRegionProcedure: str = "",renderSequenceProcedure: str = "",rendererUIName: str = "",renderingEditorsSubMenuProcedure: str = "",showBatchRenderLogProcedure: str = "",showBatchRenderProcedure: str = "",showRenderLogProcedure: str = "",startIprRenderProcedure: str = "",stopIprRenderProcedure: str = "",supportColorManagement: bool = False,textureBakingProcedure: str = "",unregisterRenderer: bool = False) -> None:
    """
    レンダーを登録するコマンドです。このコマンドを使用して、レンダラの UI 名とプロシージャ名を指定できます。また、登録したレンダラの UI 名とプロシージャ名を照会することもできます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    addGlobalsNode (string): 指定したレンダラが使用するグローバルノードを追加することができるようになります。

    -----------------------------------------

    addGlobalsTab ([string, string, string]): 指定したレンダラにコネクトされたタブを統一レンダーグローバル(RenderGlobals)ウィンドウに追加します。

    -----------------------------------------

    batchRenderOptionsProcedure (string): 指定したレンダラにコネクトされたバッチレンダーオプションのプロシージャを設定または照会します。

    -----------------------------------------

    batchRenderOptionsStringProcedure (string): バッチレンダーを行う際に、コマンドラインユーティリティ「Render」と一緒に使用する引数文字列を設定または照会します。

    -----------------------------------------

    batchRenderProcedure (string): 指定したレンダラにコネクトされたバッチレンダーのプロシージャを設定または照会します。

    -----------------------------------------

    cancelBatchRenderProcedure (string): 設定または照会すると、指定したレンダラにコネクトされた、バッチレンダーの解除のプロシージャを返します。

    -----------------------------------------

    changeIprRegionProcedure (string): 指定したレンダラにコネクトされたIPR領域の変更プロシージャを設定または照会します。

    -----------------------------------------

    commandRenderProcedure (string): 指定したレンダラにコネクトされたコマンドラインレンダリングのプロシージャを設定または照会します。

    -----------------------------------------

    exists (boolean): 指定したレンダラがレジストリに登録されている場合はtrueを、登録されていない場合はfalseを返します。

    -----------------------------------------

    globalsNodes (boolean): 指定したレンダラが使用するレンダーグローバル(RenderGlobals)ノードのリストを返します。

    -----------------------------------------

    globalsTabCreateProcNames (boolean): 指定したレンダラにコネクトされた、統一レンダーグローバル(RenderGlobals)ウィンドウのタブの作成に使用するプロシージャの名前を返します。

    -----------------------------------------

    globalsTabLabels (boolean): 指定したレンダラにコネクトされた、統一レンダーグローバル(RenderGlobals)ウィンドウのタブのラベルを返します。

    -----------------------------------------

    globalsTabUpdateProcNames (boolean): 指定したレンダラにコネクトされた、統一レンダーグローバル(RenderGlobals)ウィンドウのタブの更新に使用するプロシージャの名前を返します。

    -----------------------------------------

    iprOptionsMenuLabel (string): レンダービューのIPRメニュー下にあるIPRの更新オプションメニューのラベルを設定または照会します。

    -----------------------------------------

    iprOptionsProcedure (string): 指定したレンダラにコネクトされたIPRレンダーオプションのプロシージャを設定または照会します。

    -----------------------------------------

    iprOptionsSubMenuProcedure (string): レンダービューのIPRメニュー下にあるIPRの更新オプションメニューのサブメニューを作成するプロシージャを設定または照会します。

    -----------------------------------------

    iprRenderProcedure (string): 指定したレンダラにコネクトされたIPRレンダーコマンドを設定または照会します。

    -----------------------------------------

    iprRenderSubMenuProcedure (string): レンダービューのIPRメニュー下にあるIPRレンダーメニューのサブメニューを作成するプロシージャを設定または照会します。

    -----------------------------------------

    isRunningIprProcedure (string): 指定したレンダラにコネクトされたisRunningIprコマンドを設定または照会します。

    -----------------------------------------

    logoCallbackProcedure (string): 指定したレンダラのロゴにコネクトされたコールバックになるプロシージャを設定または照会します。たとえばロゴとコールバックは、使用するレンダラ(RenderUsing)オプションメニューの隣にある統一レンダーグローバル(RenderGlobals)ウィンドウで使用することができます。

    -----------------------------------------

    logoImageName (string): 指定したレンダラのロゴのイメージ名を設定または照会します。ロゴはレンダラを表すイメージです。

    -----------------------------------------

    materialViewRendererList (boolean): 現在登録されているマテリアルビューレンダラの名前を返します。

    -----------------------------------------

    materialViewRendererPause (boolean): マテリアルビューアを一時停止するかどうかを指定します。マテリアルビューアの更新をグローバルに停止する場合に便利です。マテリアルビューアが一時停止されている間、マテリアルビューのレンダラは中止されたままになります。

    -----------------------------------------

    materialViewRendererSuspend (boolean): マテリアルビューのレンダラを一時停止するか再開するかを指定します。別のレンダリングタスクが実行されている場合に、マテリアルビューのレンダラを一時的に停止するのに役立ちます。

    -----------------------------------------

    namesOfAvailableRenderers (boolean): 現在登録されているレンダラの名前を返します。

    -----------------------------------------

    pauseIprRenderProcedure (string): 指定したレンダラにコネクトされたIPRレンダーのキャンセルプロシージャを設定または照会します。

    -----------------------------------------

    polyPrelightProcedure (string): 指定したレンダラにコネクトされた、ポリゴンのプリライトのプロシージャを設定または照会します。

    -----------------------------------------

    refreshIprRenderProcedure (string): 指定したレンダラにコネクトされたIPRレンダーのリフレッシュプロシージャを設定または照会します。

    -----------------------------------------

    renderDiagnosticsProcedure (string): 指定したレンダラにコネクトされたレンダー診断のプロシージャを設定または照会します。

    -----------------------------------------

    renderGlobalsProcedure (string): このフラグは現在サポートされていません。次のリリースでは除去される予定です。

    -----------------------------------------

    renderMenuProcedure (string): このフラグは現在サポートされていません。次のリリースでは除去される予定です。

    -----------------------------------------

    renderOptionsProcedure (string): 指定したレンダラにコネクトされたレンダーオプションのプロシージャを設定または照会します。

    -----------------------------------------

    renderProcedure (string): 指定したレンダラにコネクトされたレンダーコマンドを設定または照会します。

    -----------------------------------------

    renderRegionProcedure (string): 指定したレンダラにコネクトされた、領域をレンダーのプロシージャを設定または照会します。

    -----------------------------------------

    renderSequenceProcedure (string): 指定したレンダラにコネクトされたシーケンスレンダリングプロシージャを設定または照会します。

    -----------------------------------------

    rendererUIName (string): 指定したレンダラのrendererUINameを設定または照会します。rendererUINameはメニューに表示されるレンダラの名前です。

    -----------------------------------------

    renderingEditorsSubMenuProcedure (string): 指定したレンダラの、レンダリングエディタ(RenderingEditors)メニュー下にある、レンダラ特有のエディタのサブメニューを作成するプロシージャを設定または照会します。

    -----------------------------------------

    showBatchRenderLogProcedure (string): 指定したレンダラにコネクトされたログファイルのバッチレンダーのプロシージャを設定または照会します。

    -----------------------------------------

    showBatchRenderProcedure (string): 指定したレンダラにコネクトされたバッチレンダーの表示のプロシージャを設定または照会します。

    -----------------------------------------

    showRenderLogProcedure (string): 指定したレンダラにコネクトされたログファイルのレンダーのプロシージャを設定または照会します。

    -----------------------------------------

    startIprRenderProcedure (string): 指定したレンダラにコネクトされたIPRレンダーの開始プロシージャを設定または照会します。

    -----------------------------------------

    stopIprRenderProcedure (string): 指定したレンダラにコネクトされたIPRレンダーの停止プロシージャを設定または照会します。

    -----------------------------------------

    supportColorManagement (boolean): レンダラでカラー管理がサポートされているかどうかを指定します。

    -----------------------------------------

    textureBakingProcedure (string): 指定したレンダラにコネクトされた、テクスチャのベイク処理のプロシージャを設定または照会します。

    -----------------------------------------

    unregisterRenderer (boolean): 指定したレンダラの登録を解除します。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def renderGlobalsNode(name: str = "",parent: str = "",renderQuality: str = "",renderResolution: str = "",shared: bool = False,skipSelect: bool = False) -> None:
    """
    このコマンドを使うと、指定タイプのディペンデンシー グラフに新規ノードを作成できます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    name (string): 新しく作成するノードの名前を設定します。ネームスペースパスを含む場合、指定されたネームスペースの下に新しいノードが作成されます。ネームスペースが存在しない場合は、ネームスペースを作成します。

    -----------------------------------------

    parent (string): DAG内で新しいノードが属する親を指定します。

    -----------------------------------------

    renderQuality (string): 精度を特定の名前のrenderQualityNodeに設定します。

    -----------------------------------------

    renderResolution (string): 解像度を特定の名前のresolutionNodeに設定します。

    -----------------------------------------

    shared (boolean): このノードは複数ファイルで共有されるため、存在していない場合のみ作成されます。

    -----------------------------------------

    skipSelect (boolean): このノードは作成後選択されません。オリジナルの選択が保持されます。

    -----------------------------------------

    Return Value:
    None: string新しいノードの名前。stringレンダー グローバル ノードの名前。
    """
    pass

    
def renderInfo(castShadows: bool = False,chordHeight: float = 1.0,chordHeightRatio: float = 1.0,doubleSided: bool = False,edgeSwap: bool = False,minScreen: float = 1.0,name: str = "",opposite: bool = False,smoothShading: bool = False,unum: int = 1,useChordHeight: bool = False,useChordHeightRatio: bool = False,useDefaultLights: bool = False,useMinScreen: bool = False,utype: int = 1,vnum: int = 1,vtype: int = 1) -> None:
    """
    renderInfo コマンドは、選択したオブジェクトのサーフェスの、ジオメトリのプロパティを設定します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    castShadows (boolean): オブジェクトによるシャドウキャスティングの有無を定義します。

    -----------------------------------------

    chordHeight (float): テッセレーションの分割基準です。

    -----------------------------------------

    chordHeightRatio (float): テッセレーションの分割基準です。

    -----------------------------------------

    doubleSided (boolean): オブジェクトが両面または片面のいずれであるかを定義します。

    -----------------------------------------

    edgeSwap (boolean): テッセレーションの分割基準です。

    -----------------------------------------

    minScreen (float): テッセレーションの分割基準です。

    -----------------------------------------

    name (string): 使用するネームスペースです。

    -----------------------------------------

    opposite (boolean): オブジェクトの法線が反転するかどうかを定義します。

    -----------------------------------------

    smoothShading (boolean): スムーズシェード(フラットシェード)をポリセットのみに適用するかどうかを定義します。

    -----------------------------------------

    unum (int): テッセレーションの分割基準です。

    -----------------------------------------

    useChordHeight (boolean): テッセレーションの分割基準です。

    -----------------------------------------

    useChordHeightRatio (boolean): テッセレーションの分割基準です。

    -----------------------------------------

    useDefaultLights (boolean): このフラグは現在サポートしていません。

    -----------------------------------------

    useMinScreen (boolean): テッセレーションの分割基準です。

    -----------------------------------------

    utype (int): テッセレーションの分割基準です。

    -----------------------------------------

    vnum (int): テッセレーションの分割基準です。

    -----------------------------------------

    vtype (int): テッセレーションの分割基準です。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def renderManip(camera: Tuple[bool, bool, bool, bool, bool] = tuple(False, False, False, False, False),light: Tuple[bool, bool, bool] = tuple(False, False, False),spotLight: Tuple[bool, bool, bool, bool, bool, bool, bool] = tuple(False, False, False, False, False, False, False),state: bool = False) -> None:
    """
    このコマンドは、カメラまたはライトのマニピュレータを作成します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    camera ([boolean, boolean, boolean, boolean, boolean]): コンポーネントカメラマニピュレータの可視状態を照会または編集します。コンポーネントの順序は、サイクルインデックス(CyclingIndex)、注視点、ピボット、クリッピングプレーン、未使用です。

    -----------------------------------------

    light ([boolean, boolean, boolean]): コンポーネントライトマニピュレータの可視状態を照会または編集します。コンポーネントの順序は、サイクルインデックス、注視点、ピボットです。

    -----------------------------------------

    spotLight ([boolean, boolean, boolean, boolean, boolean, boolean, boolean]): コンポーネントスポットライトマニピュレータの可視状態を照会または編集します。コンポーネントの順序は、サイクルインデックス、注視点、ピボット、円錐角度、周縁部、バーンドアを通した視野、減衰領域です。

    -----------------------------------------

    state (boolean): カメラ、環境光、ディレクショナルライト、ポイントライト、またはスポットライトのマニピュレータの状態を照会または編集します。このフラグの既定値はオンです。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def renderPartition() -> None:
    """
    モデルの現在のパーティションを設定または照会します。フラグ q を使用しない場合、パーティション名を引数として渡す必要があります。この場合は、現在のパーティションがその名前に設定されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    Return Value:
    None: stringレンダー パーティション。照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def renderQualityNode(name: str = "",parent: str = "",shared: bool = False,skipSelect: bool = False) -> None:
    """
    このコマンドを使うと、指定タイプのディペンデンシー グラフに新規ノードを作成できます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    name (string): 新しく作成するノードの名前を設定します。ネームスペースパスを含む場合、指定されたネームスペースの下に新しいノードが作成されます。ネームスペースが存在しない場合は、ネームスペースを作成します。

    -----------------------------------------

    parent (string): DAG内で新しいノードが属する親を指定します。

    -----------------------------------------

    shared (boolean): このノードは複数ファイルで共有されるため、存在していない場合のみ作成されます。

    -----------------------------------------

    skipSelect (boolean): このノードは作成後選択されません。オリジナルの選択が保持されます。

    -----------------------------------------

    Return Value:
    None: string新しいノードの名前。stringレンダー精度ノードの名前。
    """
    pass

    
def renderSettings(camera: str = "",customTokenString: str = "",firstImageName: bool = False,fullPath: bool = False,fullPathTemp: bool = False,genericFrameImageName: str = "",imageGenericName: bool = False,lastImageName: bool = False,layer: str = "",leaveUnmatchedTokens: bool = False) -> None:
    """
    レンダー設定(Render Settings)の共通タブのインタフェースを照会します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    camera (string): 現在のレンダリング可能なカメラを置き換えるカメラを指定します。

    -----------------------------------------

    customTokenString (string): ファイル名の中のカスタムトークンを置き換える、キーと値のカスタム対応値を指定します。firstImageNameまたはlastImageNameと一緒に使用してください。基本のトークン(Scene、Layer、RenderLayer、Camera、Version、Extension)は自動的に展開されます。その他すべてのトークンを展開するには、ここで指定する必要があります。文字列のフォーマットは、トークンと値のペアのスペース区切りリストです。たとえば、ファイル名文字列が「myFile_<myToken>_<myOtherToken>_v」の場合、このフラグ文字列に対する引数は、「myToken=myTokenValuemyOtherToken=myOtherTokenValue」の形式にする必要があります。

    -----------------------------------------

    firstImageName (boolean): 最初のイメージ名を返します。

    -----------------------------------------

    fullPath (boolean): 現在のプロジェクトを使用してイメージのフルパスを返します。firstImageName、lastImageName、genericFrameImageNameのいずれかと一緒に使用します。

    -----------------------------------------

    fullPathTemp (boolean): 現在のプロジェクトを使用してイメージのプレビューレンダーのフルパスを返します。firstImageName、lastImageName、genericFrameImageNameのいずれかと一緒に使用します。

    -----------------------------------------

    genericFrameImageName (string): 汎用フレームイメージ名を、カスタム指定したフレームインデックストークンと共に返します。

    -----------------------------------------

    imageGenericName (boolean): イメージの汎用名を返します。

    -----------------------------------------

    lastImageName (boolean): 最後のイメージ名を返します。

    -----------------------------------------

    layer (string): 現在のレンダーレイヤを置き換えるレンダーレイヤ名を指定します。

    -----------------------------------------

    leaveUnmatchedTokens (boolean): 一致しないトークンを名前文字列から除去しないでください。firstImageNameまたはlastImageNameと一緒に使用してください。

    -----------------------------------------

    Return Value:
    None: string[]コマンドの結果
    """
    pass

    
def renderThumbnailUpdate(forceUpdate: str = "") -> None:
    """
    オブジェクトのサムネールの更新を切り替えます。これらは、アトリビュート エディタやハイパーシェードなどのツールで表示できます。このコマンドを使用して true に切り替えるまで、あらゆる場所のすべてのサムネイルが更新されてオブジェクトに変更が反映されることはありません。ただし、-forceUpdate フラグを使用して特定のサムネイルを強制的にレンダリングした場合は除きます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    forceUpdate (string): サムネイルを強制的に更新します。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def renderWindowEditor(autoResize: bool = False,blendMode: int = 1,caption: str = "",changeCommand: Tuple[str, str, str, str] = tuple("", "", "", ""),clear: Tuple[int, int, float, float, float] = tuple(1, 1, 1.0, 1.0, 1.0),cmEnabled: bool = False,colorManage: bool = False,compDisplay: int = 1,compImageFile: str = "",control: bool = False,currentCamera: str = "",currentCameraRig: str = "",defineTemplate: str = "",displayImage: int = 1,displayImageViewCount: int = 1,displayStyle: str = "",docTag: str = "",doubleBuffer: bool = False,drawAxis: bool = False,editorName: bool = False,exists: bool = False,exposure: float = 1.0,filter: str = "",forceMainConnection: str = "",frameImage: bool = False,frameRegion: bool = False,gamma: float = 1.0,highlightConnection: str = "",loadImage: str = "",lockMainConnection: bool = False,mainListConnection: str = "",marquee: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),nbImages: bool = False,nextViewImage: bool = False,outputColorManage: bool = False,panel: str = "",parent: str = "",pcaption: str = "",realSize: bool = False,refresh: bool = False,removeAllImages: bool = False,removeImage: bool = False,resetRegion: bool = False,resetViewImage: bool = False,saveImage: bool = False,scaleBlue: float = 1.0,scaleGreen: float = 1.0,scaleRed: float = 1.0,selectionConnection: str = "",showRegion: Tuple[int, int] = tuple(1, 1),singleBuffer: bool = False,snapshot: Tuple[str, int, int] = tuple("", 1, 1),snapshotMode: bool = False,stateString: bool = False,stereo: int = 1,stereoImageOrientation: Tuple[str, str] = tuple("", ""),stereoMode: str = "",toggle: bool = False,unParent: bool = False,unlockMainConnection: bool = False,updateMainConnection: bool = False,useTemplate: str = "",viewImageCount: int = 1,viewTransformName: str = "",writeImage: str = "") -> None:
    """
    レンダリング プロセスの結果を受け取ることのできるエディタ ウインドウを作成します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    autoResize (boolean): レンダービューエディタがビューポートのサイズを自動的に変更するかしないかを設定します。

    -----------------------------------------

    blendMode (int): レンダービューをブレンドモードに設定します。レンダービューに送信された新しいイメージがレンダービューで前のイメージとブレンドされて、合成されたイメージが表示されます。

    -----------------------------------------

    caption (string): レンダービューの下部に表示されるキャプションを設定します。

    -----------------------------------------

    changeCommand ([string, string, string, string]): パラメータ:先頭文字列:command2番目の文字列:editorName3番目の文字列:editorCmd4番目の文字列:updateFuncエディタで何らかの変更を行う場合にこのコマンドをコールします。このコマンドの基本形は次のとおりです:command(string$editor,string$editorCmd,string$updateFunc,int$reason)考えられる理由は次のとおりです。0:特に理由なし1:スケールカラー2:バッファ(シングル/ダブル)3:軸4:表示されたイメージ5:メモリに保存されたイメージ

    -----------------------------------------

    clear ([int, int, float, float, float]): 指定した解像度、指定したカラーで、画像を鮮明にします。引数はそれぞれ幅、高さ、赤、緑、青です。

    -----------------------------------------

    cmEnabled (boolean): ビューでのカラー管理の適用をオンまたはオフにします。設定すると、現在のビューに設定されているカラー管理設定が使用されます。

    -----------------------------------------

    colorManage (boolean): writeImageフラグと一緒に使用すると、書き込まれたイメージはビューに付属するビューカラーマネージャの設定を使用してカラー管理されます。

    -----------------------------------------

    compDisplay (int): 0:合成を無効にします。1:合成されたイメージを直ちに表示します。たとえば、フォアグラウンドレイヤタイルがレンダービューウィンドウに送信された場合、合成されたタイルがレンダービューウィンドウに表示され、元のフォアグラウンドレイヤタイルは表示されません。2:合成されていないイメージが表示され、その後のコマンドのために合成されたイメージを保持します。たとえば、フォアグラウンドレイヤタイルがレンダービューウィンドウに送信された場合、元のフォアグラウンドレイヤタイルは表示されず、合成されたタイルはバッファに格納されます。3:現在の合成されたイメージを表示します。合成されたイメージがバッファに存在する場合は、これを表示します。

    -----------------------------------------

    compImageFile (string): 指定したイメージファイルを開き、イメージをレンダーする場合と同様にバッファでブレンドします。

    -----------------------------------------

    control (boolean): 照会モード専用です。このエディタの最上位のコントロールを返します。通常は、親を取得してポップアップメニューをアタッチするために使用します。注意:コントロールのないエディタが存在する場合があります。コントロールが存在しない場合は、この照会はNONEを返します。

    -----------------------------------------

    currentCamera (string): 現在のカメラを取得または設定します(直前のレンダーを再実行するときに使用)。

    -----------------------------------------

    currentCameraRig (string): 現在のカメラのリグの名前を取得または設定します。カメラリグが指定されている場合、currentCameraの値とは対照的に、最後のレンダリングを再実行するときに使用されます。currentCameraの値は、カメラリグのレンダリングに最後に使用された子カメラを保持します。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    displayImage (int): 特定のイメージをエディタイメージスタックで現在のエディタイメージとして設定します。イメージは、「si/saveImage」フラグを使用してエディタイメージスタックに追加されます。

    -----------------------------------------

    displayImageViewCount (int): 指定したイメージに対して格納されたビューの数をエディタイメージスタックに照会します。これは、現在のレンダリングイメージに対するビューの数を返す「viewImageCount」を使用した照会とは異なります。

    -----------------------------------------

    displayStyle (string): イメージを表示するモードを設定します。有効な値は、基本RGBイメージを表示する場合は「カラー」マスクチャネルを表示する場合は「マスク」イメージの輝度を表示する場合は「輝度」

    -----------------------------------------

    docTag (string): エディタにタグをアタッチします。

    -----------------------------------------

    doubleBuffer (boolean): 表示をダブルバッファモードに設定します。

    -----------------------------------------

    drawAxis (boolean): 軸が描画されるかどうかを設定または照会します。

    -----------------------------------------

    editorName (boolean): エディタの名前を返します。エディタがまだ作成されていない場合は、空の文字列を返します。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    exposure (float): 現在のビューのカラー管理に使用される露出値です。

    -----------------------------------------

    filter (string): このエディタに使用する項目フィルタオブジェクトの名前を指定します。エディタの主要リストに表示される情報をフィルタします。

    -----------------------------------------

    forceMainConnection (string): エディタがコンテンツのソースとして使用するselectionConnectionオブジェクトの名前を指定します。エディタはselectionConnectionオブジェクトに含まれている項目のみを表示します。これは-mainListConnectionフラグの変形で、接続がロックされている場合でも強制的に変更します。このフラグを使用して、-unlockMainConnection、-mainListConnection、-lockMainConnectionフラグを直後に連続して使用する場合に、オーバーヘッドを減します。

    -----------------------------------------

    frameImage (boolean): 画像をウィンドウの中に収めます。

    -----------------------------------------

    frameRegion (boolean): 領域をウィンドウの中に収めます。

    -----------------------------------------

    gamma (float): 現在のビューのカラー管理に使用されるガンマ値です。

    -----------------------------------------

    highlightConnection (string): そのハイライトリストをエディタと同期化させるselectionConnectionオブジェクトの名前を指定します。すべてのエディタにハイライトリストがあるわけではありません。ハイライトリストがあるエディタの場合、これは第二の選択項目を表示したリストになります。

    -----------------------------------------

    loadImage (string): ディスクからイメージをロードして現在のエディタイメージとして設定します。

    -----------------------------------------

    lockMainConnection (boolean): mainConnection内のオブジェクトの現在のリストをロックして、そのオブジェクトだけがエディタ内に表示されるようにします。これ以降、元のmainConnectionに変更を加えても無視されます。

    -----------------------------------------

    mainListConnection (string): エディタがコンテンツのソースとして使用するselectionConnectionオブジェクトの名前を指定します。エディタはselectionConnectionオブジェクトに含まれている項目のみを表示します。

    -----------------------------------------

    marquee ([float, float, float, float]): 引数は長方形の4つのコーナー(左、右、下、上)を定義します。この長方形はレンダー計算のセレクションボックスを定義します。

    -----------------------------------------

    nbImages (boolean): イメージの数を返します。

    -----------------------------------------

    nextViewImage (boolean): レンダーエディタは、単一ビューの中で複数のカメラをレンダリングすることができます。これはイメージが保存されるイメージビニングとは異なります。2つの異なるカメラレンダーを隣り合わせに並べて比較するには、複数のイメージビューが便利です。nextViewImageフラグを使用すると、エディタに対して、内部格納メカニズムの準備を行って次のビュー位置に格納するよう通知されます。

    -----------------------------------------

    outputColorManage (boolean): writeImageフラグと一緒に使用すると、書き込まれたイメージは、ビューにアタッチされたカラープリファレンス内の出力カラースペースを使用してカラー管理されます。

    -----------------------------------------

    panel (string): このエディタ用のパネルを指定します。既定では、エディタがスクリプトパネルの作成コールバックで作成された場合、エディタはそのパネルに属します。エディタがパネルに属していない場合、エディタのあるウィンドウを削除するとエディタも削除されます。

    -----------------------------------------

    parent (string): このエディタの親のレイアウトを指定します。このフラグは、エディタが現在ペアレント化されていない場合のみに効果があります。

    -----------------------------------------

    pcaption (string): 現在、レンダーエディタに表示されているイメージの下に表示される恒久的なキャプションを取得または設定します。

    -----------------------------------------

    realSize (boolean): 画像をピクセル等倍で表示します。

    -----------------------------------------

    refresh (boolean): 現在のエディタイメージのリフレッシュを要求します。

    -----------------------------------------

    removeAllImages (boolean): エディタイメージスタックからすべてのエディタイメージを除去します。

    -----------------------------------------

    removeImage (boolean): エディタイメージスタックから現在のエディタイメージを除去します。

    -----------------------------------------

    resetRegion (boolean): マーキー/領域を強制的にリセットします。

    -----------------------------------------

    resetViewImage (boolean): レンダーエディタは、単一ビューの中で複数のカメラをレンダリングすることができます。これはイメージが保存されるイメージビニングとは異なります。2つの異なるカメラレンダーを隣り合わせに並べて比較するには、複数のイメージビューが便利です。resetViewImageフラグを使用すると、エディタの内部格納メカニズムを最初のイメージにリセットすることができます。これはレンダービューレンダーの一番最初に行われます。

    -----------------------------------------

    saveImage (boolean): メモリに現在のEditorImageを保存します。保存されたエディタイメージは、エディタイメージスタックに格納されます。最も新しく保存したイメージは0の位置に、次に新しく保存したイメージは1の位置、などと格納されます。現在のエディタイメージを前に保存したイメージに設定するには、「di/displayImage」フラグを使用します。

    -----------------------------------------

    scaleBlue (float): ビュー内の青の成分のスケーリング係数を定義します。既定値は1で、-1000から+1000までが可能です。

    -----------------------------------------

    scaleGreen (float): ビュー内の緑の成分のスケーリング係数を定義します。既定値は1で、-1000から+1000までが可能です。

    -----------------------------------------

    scaleRed (float): ビュー内の赤の成分のスケーリング係数を定義します。既定値は1で、-1000から+1000までが可能です。

    -----------------------------------------

    selectionConnection (string): その独自のセレクションリストをエディタと同期化させるselectionConnectionオブジェクトの名前を指定します。このエディタから選択する場合、selectionConnectionオブジェクトの中から選択します。オブジェクトが変更されると、エディタが更新されて変更が反映されます。

    -----------------------------------------

    showRegion ([int, int]): 指定した解像度で現在の領域を表示します。2つのパラメータは幅と高さを定義します。

    -----------------------------------------

    singleBuffer (boolean): 表示をシングルバッファモードに設定します。

    -----------------------------------------

    snapshot ([string, int, int]): 指定したサイズでモデルエディタのカメラのコピーを作成します。最初の引数はエディタ名、2番目は幅、3番目は高さです。

    -----------------------------------------

    snapshotMode (boolean): ウィンドウのスナップショットモードを取得または設定します。

    -----------------------------------------

    stateString (boolean): 照会モード専用のフラグです。エディタを作成して現在のエディタの状態と一致させるMELコマンドを返します。返されたコマンド文字列は、指定した名前の代わりに文字列変数$editorNameを使用します。

    -----------------------------------------

    stereo (int): エディタを立体視イメージモードにします。出力イメージの解像度を水平サイズの2倍にすると効果的です。イメージの方向は、stereoOrientationフラグを使用して設定します。

    -----------------------------------------

    stereoImageOrientation ([string, string]): 立体視カメラレンダーの方向を指定します。1番目の引数はfirstleftイメージの方向の値を、2番目の引数はrightイメージの方向の値を指定します。方向の値は「normal」(カメラを通じてみたように表示される)、または「mirrored」(水平方向にミラーリングされる)です。

    -----------------------------------------

    stereoMode (string): イメージをビューに表示する方法を指定します。既定は「stereo」で、イメージは隣り合わせにレンダーされます。「both」では、レンダーされるイメージは単一のイメージで、通常のイメージのサイズの2倍です。その他の表示方法には「redcyan」、「redcyanlum」、「leftonly」、「rightonly」、または「stereo」があります。both-左側と右側の両方を表示します。redcyan-イメージを赤とシアンのペアとして表示します。redcyanlum-イメージの輝度を赤とシアンのペアとして表示します。leftonly-左側のみ表示します。rightonly-右側のみ表示します。stereo-CrystalEyes(tm)またはZscreen(tm)レンダーをサポートするモードです。

    -----------------------------------------

    toggle (boolean): 地表プレーン表示のオン/オフを切り替えます。

    -----------------------------------------

    unParent (boolean): エディタをそのレイアウトから除去するように指定します。これは照会モードでは使用できません。

    -----------------------------------------

    unlockMainConnection (boolean): mainConnectionをロック解除して、オリジナルのmainConnection(まだ使用可能な場合)を効率的に復元し、ダイナミックな更新を行います。

    -----------------------------------------

    updateMainConnection (boolean): ロックされたmainConnectionをオリジナルのmainConnectionから更新させますが、ロック状態は保持されます。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    viewImageCount (int): レンダーエディタは、単一ビューの中で複数のカメラをレンダリングすることができます。これはイメージが保存されるイメージビニングとは異なります。2つの異なるカメラレンダーを隣り合わせに並べて比較するには、複数のイメージビューが便利です。viewImageCountフラグを使用すると、エディタに対して、内部イメージ格納メカニズムの準備を行って指定されたビューの数に対応するよう通知されます。

    -----------------------------------------

    viewTransformName (string): 現在のビューでカラー管理が有効になっている場合に適用されるビュートランスフォームを設定/取得します。

    -----------------------------------------

    writeImage (string): ディスクに現在のエディタイメージを書き込みます。

    -----------------------------------------

    Return Value:
    None: stringエディタの名前照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def resolutionNode(name: str = "",parent: str = "",shared: bool = False,skipSelect: bool = False) -> None:
    """
    このコマンドを使うと、指定タイプのディペンデンシー グラフに新規ノードを作成できます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    name (string): 新しく作成するノードの名前を設定します。ネームスペースパスを含む場合、指定されたネームスペースの下に新しいノードが作成されます。ネームスペースが存在しない場合は、ネームスペースを作成します。

    -----------------------------------------

    parent (string): DAG内で新しいノードが属する親を指定します。

    -----------------------------------------

    shared (boolean): このノードは複数ファイルで共有されるため、存在していない場合のみ作成されます。

    -----------------------------------------

    skipSelect (boolean): このノードは作成後選択されません。オリジナルの選択が保持されます。

    -----------------------------------------

    Return Value:
    None: string新しいノードの名前。stringレンダー解像度ノードの名前
    """
    pass

    
def sampleImage(fastSample: bool = False,resolution: Tuple[int, str] = tuple(1, "")) -> None:
    """
    sampleImage コマンドを使用して、マルチリスタ内のスウォッチなどのサンプル イメージのパラメータを制御します。fast オプションをオンに設定すると、レンダー時間が短縮される代わりにエッジの外観がギザギザになります。resolution オプションには、指定したノードのレンダーされるイメージの幅をピクセル単位で指定します。サンプル イメージは正方形なので、イメージの幅はイメージの高さでもあります。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    fastSample (boolean): 高速だが粗いレンダリングを使用する場合

    -----------------------------------------

    resolution ([int, name]): このフラグの1番目の引数には、解像度をピクセル単位で指定します。2番目の引数には、ディペンデンシーノードを指定します。このフラグを指定すると、指定したノードに対する以後のサンプルイメージのレンダリングは指定した解像度で行われます。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def setDefaultShadingGroup() -> None:
    """
    setDefaultShadingGroup コマンドは、どのシェーディング グループを現在の既定シェーディング グループとみなすかを変更するために使用します。以降に作成されるオブジェクトは、新しい既定のグループに割り当てられます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def shadingConnection(connectionState: bool = False) -> None:
    """
    ェーデイングで使用されるノード間の接続の接続状態を設定します。接続の接続先のアトリビュートを指定します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    connectionState (boolean): 接続の状態を指定します。On/True/1は接続がアクティブであることを意味し、Off/False/0は接続が非アクティブであることを意味します。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def shadingNetworkCompare(byName: bool = False,byValue: bool = False,delete: bool = False,equivalent: bool = False,network1: bool = False,network2: bool = False,upstreamOnly: bool = False) -> None:
    """
    2 つのシェーディング ネットワークを比較します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    byName (boolean): 比較する際に、ノード名を考慮するかどうかを指定します。trueの場合、2つのシェーディングネットワークは、対応するノード名が同じである場合のみに(ネームスペースは無視します)、同等に扱われます。falseの場合、2つのシェーディングネットワークは、対応するノード名が違っていても、同等に扱われます。既定はfalseです。

    -----------------------------------------

    byValue (boolean): 比較する際に、接続されていないアトリビュートの値を考慮するかどうかを指定します。trueの場合、2つのシェーディングネットワークは、対応する接続されていないアトリビュートが同じ型で同じ値を持つ場合のみに、同等に扱われます。int、bool、float、string型のアトリビュートのみの値を比較します。falseの場合、2つのシェーディングネットワークは、対応する接続されていないアトリビュートの型や値が違っていても、同等に扱われます。既定はtrueです。

    -----------------------------------------

    delete (boolean): 指定した比較をメモリから消去します。

    -----------------------------------------

    equivalent (boolean): intを返します。比較の結果、シェーディングネットワークが同等の場合は1を返し、そうでない場合は0を返します。

    -----------------------------------------

    network1 (boolean): string[]を返します。比較の結果、シェーディングネットワークが同等の場合は空の文字配列を返し、そうでない場合は1番目のシェーディングネットワークのノードを返します。

    -----------------------------------------

    network2 (boolean): string[]を返します。比較の結果、シェーディングネットワークが同等の場合は空の文字配列を返し、そうでない場合は2番目のシェーディングネットワークのノードを返します。

    -----------------------------------------

    upstreamOnly (boolean): 比較する際に、シェーディングネットワークノードの下流に接続されたノードを考慮するかどうかを指定します。trueの場合、シェーディンググループの上流にあるノードのみを考慮します。下流接続のみをたどり、ノードからシェーディンググループ上のシェーダアトリビュートへの接続パスが存在しない場合、ノードは考慮されません。falseの場合、シェーディンググループのシェーダアトリビュートへの入力接続が末端にある上流または下流接続をたどって、接続パスが見つかるとノードを考慮します。これらの「ぶら下がった」ノードは、シェーディンググループのカラー、ディスプレイスメント、ボリュームなどの特性には直接寄与しません。既定はfalseです。

    -----------------------------------------

    Return Value:
    None: string[]|string|intコマンドの結果照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def shadingNode(asLight: bool = False,asPostProcess: bool = False,asRendering: bool = False,asShader: bool = False,asTexture: bool = False,asUtility: bool = False,isColorManaged: bool = False,name: str = "",parent: str = "",shared: bool = False,skipSelect: bool = False) -> None:
    """
    このコマンドを使うと、指定タイプのディペンデンシー グラフに新規ノードを作成できます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    asLight (boolean): 現在のDGノードをライトとして分類します。

    -----------------------------------------

    asPostProcess (boolean): 現在のDGノードをポストプロセスとして分類します。

    -----------------------------------------

    asRendering (boolean): 現在のDGノードをレンダリングノードとして分類します。

    -----------------------------------------

    asShader (boolean): 現在のDGノードをシェーダとして分類します。

    -----------------------------------------

    asTexture (boolean): 現在のDGノードをテクスチャとして分類します。

    -----------------------------------------

    asUtility (boolean): 現在のDGノードをユーティリティとして分類します。

    -----------------------------------------

    isColorManaged (boolean): 現在のDGノードをカラー管理対象として分類します。

    -----------------------------------------

    name (string): 新しく作成するノードの名前を設定します。ネームスペースパスを含む場合、指定されたネームスペースの下に新しいノードが作成されます。ネームスペースが存在しない場合は、ネームスペースを作成します。

    -----------------------------------------

    parent (string): DAG内で新しいノードが属する親を指定します。

    -----------------------------------------

    shared (boolean): このノードは複数ファイルで共有されるため、存在していない場合のみ作成されます。

    -----------------------------------------

    skipSelect (boolean): このノードは作成後選択されません。オリジナルの選択が保持されます。

    -----------------------------------------

    Return Value:
    None: string新しいノードの名前。string(新しいノードの名前)
    """
    pass

    
def showShadingGroupAttrEditor() -> None:
    """
    showShadingGroupAttrEditor コマンドは、現在のオブジェクトのシェーディング グループ情報に関する アトリビュート エディタを開きます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    Return Value:
    None: booleanシェーディング グループが表示される場合は true 、それ以外の場合は false。照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def soloMaterial(attr: str = "",last: bool = False,node: str = "",unsolo: bool = False) -> None:
    """
    指定したマテリアル ノードの出力アトリビュートのプレビューを表示します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    attr (string): ノードのアトリビュートをソロに指定します。

    -----------------------------------------

    last (boolean): 最後のマテリアルノードおよびアトリビュートをソロ化するかどうかを指定します。

    -----------------------------------------

    node (string): ノードをソロに指定します。

    -----------------------------------------

    unsolo (boolean): ソロ化を解除するかどうかを指定します。

    -----------------------------------------

    Return Value:
    None: boolean成功または失敗照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def surfaceSampler(camera: str = "",fileFormat: str = "",filename: str = "",filterSize: float = 1.0,filterType: int = 1,flipU: bool = False,flipV: bool = False,ignoreMirroredFaces: bool = False,ignoreTransforms: bool = False,mapHeight: int = 1,mapMaterials: bool = False,mapOutput: str = "",mapSpace: str = "",mapWidth: int = 1,maxSearchDistance: float = 1.0,maximumValue: float = 1.0,overscan: int = 1,searchCage: str = "",searchMethod: int = 1,searchOffset: float = 1.0,shadows: bool = False,source: str = "",sourceUVSpace: str = "",superSampling: int = 1,target: str = "",targetUVSpace: str = "",useGeometryNormals: bool = False,uvSet: str = "") -> None:
    """
    サーフェスのディテールを、ソース サーフェスからターゲット サーフェスの新しいテクスチャ マップにマップします。コマンドを起動するときに、両方のオブジェクトを選択する必要があります。まずソース サーフェスを選択してから、ターゲットを選択してください。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    camera (name): スペキュラハイライトまたは反射のような、カメラの特定のライティングの計算に使用するカメラを指定します。

    -----------------------------------------

    fileFormat (string): 「dds」などのファイル拡張子で表すイメージフォーマットです。これは出力マップを指定するたびに1度は含める必要があります。

    -----------------------------------------

    filename (string): マップを作成する時に使用するファイル名です。これは出力マップを指定するたびに1度は含める必要があります。

    -----------------------------------------

    filterSize (float): フィルタサイズ(ピクセルで表示)です。2.0を超えるような大きな値ではより滑らかでソフトになり、1.0に近い値ではよりシャープになります。

    -----------------------------------------

    filterType (uint): 使用するフィルタタイプです。0はGaussianフィルタ、1は三角形のフィルタ、2はボックスフィルタです。

    -----------------------------------------

    flipU (boolean): 生成されたイメージのU座標を反転します。

    -----------------------------------------

    flipV (boolean): 生成されたイメージのV座標を反転します。

    -----------------------------------------

    ignoreMirroredFaces (boolean): 反転した(ミラーされた)フェースがマップの生成に寄与しなくなります。

    -----------------------------------------

    ignoreTransforms (boolean): トランスフォームを使用する(ワールド空間で検索を実行する)か、または使用しない(オブジェクト空間で検索を実行する)かを制御します。

    -----------------------------------------

    mapHeight (uint): 生成したマップのピクセル幅です。これは出力マップを指定するたびに1度は含める必要があります。

    -----------------------------------------

    mapMaterials (boolean): 必要に応じて(法線マップなどの場合)、マップアトリビュートをサンプリングするときにマテリアルを含めるかどうかを制御します。これは出力マップを指定するたびに1度は含める必要があります。

    -----------------------------------------

    mapOutput (string): 作成する新しい出力マップを指定します。「normal」、「displacement」、「diffuseRGB」、「litAndShadedRGB」、「alpha」のいずれかです。

    -----------------------------------------

    mapSpace (string): マップを生成する空間です。有効なキーワードは「object」です。既定は接線空間です。これは出力マップを指定するたびに1度は含める必要があります。

    -----------------------------------------

    mapWidth (uint): 生成したマップのピクセル幅です。出力イメージフォーマットによっては、等倍または2乗のピクセル幅が必要です。これは出力マップを指定するたびに1度は含める必要があります。

    -----------------------------------------

    maxSearchDistance (linear): ソースサーフェスを検索するターゲットサーフェスからの最大距離を制御します。値「0」は、無制限を示します。生成したマップにオブジェクトの反対側のアーティファクトが含まれる場合は、この値をオブジェクトの半径とほぼ同じ距離に設定してください。このフラグを含む場合は、すべてのターゲットに1度は含める必要があります。

    -----------------------------------------

    maximumValue (linear): マップに含むことができる最大値です。これによって、ディスプレイスメントなどの浮動小数点の値が整数イメージフォーマットに量子化される方法をコントロールすることができます。

    -----------------------------------------

    overscan (uint): UV境界の周囲をレンダーするための追加のピクセル数です。これはUVの継ぎ目のテクセルフィルタリングアーティファクトを最低限に抑えるのに役立ちます。テクスチャにMipmapを生成する場合は、filterSizeを1より大きくして、さらに値を大きくする必要があることがあります。

    -----------------------------------------

    searchCage (string): ソースサーフェスを検索するときのガイドとして使用する、検索エンベロープサーフェスを指定します。このフラグを含む場合は、すべてのターゲットに1度は含める必要があります。

    -----------------------------------------

    searchMethod (uint): ターゲットサーフェスのサンプリングポイントとソースのポイントを一致させるために使用する検索手法を制御します。0はエンベロープに最も近く、1はエンベロープの外側の交差よりも内側の交差を優先し、2はエンベロープの内側の交差のみ使用します。

    -----------------------------------------

    searchOffset (linear): ソースサーフェスを検索するときのスタートポイントとして使用する、固定オフセットをターゲットサーフェスから指定します。この値は、所定のターゲットに検索ケージが指定されていない場合のみ使用します。このフラグを含む場合は、すべてのターゲットに1度は含める必要があります。

    -----------------------------------------

    shadows (boolean): 必要に応じて(ライティングおよびシェーディングなどの場合)、計算にシャドウを含めるかどうかを制御します。現在は深度マップシャドウのみがサポートされています。

    -----------------------------------------

    source (string): サンプリングソースとして使用するサーフェスを指定します。

    -----------------------------------------

    sourceUVSpace (string): サーフェス間のデータ転送をUV空間内で行うことを指定し、転送空間として使用するソースサーフェス上のUVセットの名前を指定します。

    -----------------------------------------

    superSampling (uint): 各出力値向用に計算されたサンプリングポイントの数を制御します。このアルゴリズムでは各ポイントに2のn乗の2乗のサンプルを使用します(値が0の場合は単一のサンプルを使用し、値が3の場合は各ポイントに64のサンプルという計算です)。

    -----------------------------------------

    target (string): 出力情報をサンプリングするサーフェスを指定します。

    -----------------------------------------

    targetUVSpace (string): サーフェス間のデータ転送をUV空間内で行うことを指定し、転送空間として使用するターゲットサーフェス上のUVセットの名前を指定します。

    -----------------------------------------

    useGeometryNormals (boolean): サーフェスの検索にジオメトリ法線とサーフェス法線のどちらを使用するかを制御します。ジオメトリ法線を使用すると確実に滑らかなマッピングになりますが、ソース/ターゲットサーフェス間の距離が開いている場合は、歪んだマッピングになる可能性があります。サーフェス法線を使用すると、マッピングが重なったり途切れたりする可能性がありますが、マッピングをサーフェス法線の方向に歪ませることができます。

    -----------------------------------------

    uvSet (string): 出力マップを作成する時に使用するUVセットの名前です。このフラグを含む場合は、すべてのターゲットに1度は含める必要があります。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def surfaceShaderList(add: str = "",remove: str = "") -> None:
    """
    オブジェクトと現在のシェーディング グループ間のリレーションシップを追加/除去します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    add (name): オブジェクトをシェーダグループのリストに追加します。

    -----------------------------------------

    remove (name): オブジェクトをシェーダグループのリストから除去します。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def swatchRefresh() -> None:
    """
    swatchRefresh コマンドは、画面のイメージ ソース ノード スウォッチをリフレッシュします。このコマンドンの目的は、ディペンデンシー グラフでダーティな伝搬がない場合に、スウォッチのリフレッシュをトリガするメカニズムを提供することです。このコマンドは imageSource-derived ノード タイプと一緒の場合のみ機能します。引数なしでこのコマンドを起動すると、すべての imageSource スウォッチがリフレッシュされます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    Return Value:
    None: booleanすべての引数が有効なイメージ ソース ノードであり操作が成功してる場合は true です。
    """
    pass

    
def textureWindow(activeSelectionOnTop: bool = False,axesColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),backFacingColor: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),capture: str = "",captureSequenceNumber: int = 1,changeCommand: Tuple[str, str, str, str] = tuple("", "", "", ""),checkerColor1: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),checkerColor2: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),checkerColorMode: int = 1,checkerDensity: int = 1,checkerDrawTileLabels: bool = False,checkerGradient1: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),checkerGradient2: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),checkerGradientOverlay: bool = False,checkerTileLabelColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),clearImage: bool = False,cmEnabled: bool = False,control: bool = False,defineTemplate: str = "",displayAxes: bool = False,displayCheckered: bool = False,displayDistortion: bool = False,displayDivisionLines: bool = False,displayGridLines: bool = False,displayImage: int = 1,displayIsolateSelectHUD: bool = False,displayLabels: bool = False,displayOverlappingUVCountHUD: bool = False,displayPreselection: bool = False,displayReversedUVCountHUD: bool = False,displaySolidMap: bool = False,displayStyle: str = "",displayTextureBorder: bool = False,displayUVPositionHUD: bool = False,displayUVShellCountHUD: bool = False,displayUVStatisticsHUD: bool = False,displayUsedPercentageHUD: bool = False,distortionAlpha: float = 1.0,distortionPerObject: bool = False,divisions: int = 1,docTag: str = "",doubleBuffer: bool = False,drawAxis: bool = False,drawSubregions: bool = False,exists: bool = False,exposure: float = 1.0,filter: str = "",forceMainConnection: str = "",forceRebake: bool = False,frameAll: bool = False,frameSelected: bool = False,frontFacingColor: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),gamma: float = 1.0,gridLinesColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),gridNumbersColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),highlightConnection: str = "",imageBaseColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),imageDim: bool = False,imageDisplay: bool = False,imageNames: bool = False,imageNumber: int = 1,imagePixelSnap: bool = False,imageRatio: bool = False,imageRatioValue: float = 1.0,imageSize: bool = False,imageTileRange: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),imageUnfiltered: bool = False,internalFaces: bool = False,labelPosition: str = "",loadImage: str = "",lockMainConnection: bool = False,mainListConnection: str = "",maxResolution: int = 1,multiColorAlpha: float = 1.0,nbImages: bool = False,nextView: bool = False,numUvSets: bool = False,numberOfImages: int = 1,numberOfTextures: int = 1,panel: str = "",parent: str = "",previousView: bool = False,realSize: bool = False,refresh: bool = False,relatedFaces: bool = False,removeAllImages: bool = False,removeImage: bool = False,rendererString: str = "",reset: bool = False,saveImage: bool = False,scaleBlue: float = 1.0,scaleGreen: float = 1.0,scaleRed: float = 1.0,selectInternalFaces: bool = False,selectRelatedFaces: bool = False,selectionConnection: str = "",setUvSet: int = 1,singleBuffer: bool = False,size: float = 1.0,solidMap3dView: bool = False,solidMapColorSeed: int = 1,solidMapPerShell: bool = False,spacing: float = 1.0,stateString: bool = False,style: int = 1,subdivisionLinesColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),textureBorder3dView: bool = False,textureBorderColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),textureBorderWidth: int = 1,textureNames: bool = False,textureNumber: int = 1,tileLabels: bool = False,tileLinesColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),toggle: bool = False,toggleExposure: bool = False,toggleGamma: bool = False,unParent: bool = False,unlockMainConnection: bool = False,updateMainConnection: bool = False,useFaceGroup: bool = False,useTemplate: str = "",usedPercentageHUDRange: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),uvSets: bool = False,viewPortImage: bool = False,viewTransformName: str = "",wireframeComponentColor: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),wireframeObjectColor: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),writeImage: str = "") -> None:
    """
    このコマンドは、UV エディタの作成およびテクスチャ エディタの設定の照会および編集に使用されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    activeSelectionOnTop (boolean): その他のものの上にソリッドマップやアクティブな選択の歪みを表示します。

    -----------------------------------------

    axesColor ([float, float, float]): 軸の色です。既定は0.00.01.0です。

    -----------------------------------------

    backFacingColor ([float, float, float, float]): RGBAバックフェース側のカラーを設定または照会します。

    -----------------------------------------

    capture (string): ディスク上の指定したイメージファイルにビューポートのキャプチャを1回実行します。

    -----------------------------------------

    captureSequenceNumber (int): 0以上の値を指定すると、「capture」フラグが有効な場合、以降にリフレッシュするたびにイメージファイルがディスクに保存されます。「capture」フラグの引数に{ルート名}.{拡張子}という名前が使用されている場合、ファイル名は{ルート名}.#.{拡張子}になります。#の値はこの引数に指定した値から開始し、以降にリフレッシュするたびに増分します。「capture」フラグに0未満の値または空のファイル名を指定すると、シーケンスキャプチャを無効にできます。

    -----------------------------------------

    changeCommand ([string, string, string, string]): パラメータ:先頭文字列:command2番目の文字列:editorName3番目の文字列:editorCmd4番目の文字列:updateFuncエディタで何らかの変更を行う場合にこのコマンドをコールします。このコマンドの基本形は次のとおりです:command(string$editor,string$editorCmd,string$updateFunc,int$reason)考えられる理由は次のとおりです。0:特に理由なし1:スケールカラー2:バッファ(シングル/ダブル)3:軸4:表示されたイメージ5:メモリに保存されたイメージ

    -----------------------------------------

    checkerColor1 ([float, float, float]): カラーモードが「2-colors」の場合に、チェッカと識別パターンの第1カラーを設定します。

    -----------------------------------------

    checkerColor2 ([float, float, float]): カラーモードが「2-colors」の場合に、チェッカと識別パターンの第2カラーを設定します。

    -----------------------------------------

    checkerColorMode (int): チェッカと識別パターンのカラーモードを設定します。0:multi-colors、1:2-colors。

    -----------------------------------------

    checkerDensity (int): チェッカと識別パターンの密度を設定します。

    -----------------------------------------

    checkerDrawTileLabels (boolean): チェッカタイルのラベル表示を切り替えます。

    -----------------------------------------

    checkerGradient1 ([float, float, float]): カラーモードが「2-colors」の場合に、チェッカと識別パターンの第1グラデーションを設定します。

    -----------------------------------------

    checkerGradient2 ([float, float, float]): カラーモードが「2-colors」の場合に、チェッカと識別パターンの第2グラデーションを設定します。

    -----------------------------------------

    checkerGradientOverlay (boolean): グラデーションの適用を切り替えます。

    -----------------------------------------

    checkerTileLabelColor ([float, float, float]): チェッカタイルのラベルのカラーを設定します。

    -----------------------------------------

    clearImage (boolean): 現在のエディタイメージをクリアします。

    -----------------------------------------

    cmEnabled (boolean): エディタでのカラー管理の適用をオンまたはオフにします。設定すると、現在のエディタに設定されているカラー管理設定が使用されます。

    -----------------------------------------

    control (boolean): 照会モード専用です。このエディタの最上位のコントロールを返します。通常は、親を取得してポップアップメニューをアタッチするために使用します。注意:コントロールのないエディタが存在する場合があります。コントロールが存在しない場合は、この照会はNONEを返します。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    displayAxes (boolean): グリッド軸を表示するには、trueを指定します。

    -----------------------------------------

    displayCheckered (boolean): 各UVタイルに対して一意のチェッカと識別パターンを表示します。

    -----------------------------------------

    displayDistortion (boolean): レイアウトをシェーディングカラーで表示して、領域を伸長/収縮されたUVであると特定します。

    -----------------------------------------

    displayDivisionLines (boolean): グリッドラインの間のサブディビジョンラインを表示するには、trueを指定します。

    -----------------------------------------

    displayGridLines (boolean): グリッドラインを表示するには、trueを指定します。

    -----------------------------------------

    displayImage (int): 特定のイメージをエディタイメージスタックで現在のエディタイメージとして設定します。イメージは、「si/saveImage」フラグを使用してエディタイメージスタックに追加されます。

    -----------------------------------------

    displayIsolateSelectHUD (boolean): 分離表示された選択項目をヘッズアップ表示に表示します。

    -----------------------------------------

    displayLabels (boolean): trueを指定してグリッドラインの数字ラベルを表示します。

    -----------------------------------------

    displayOverlappingUVCountHUD (boolean): オーバーラップUV数を部分UV統計HUDとしてヘッズアップ表示に表示します。

    -----------------------------------------

    displayPreselection (boolean): 事前選択表示を切り替えます。

    -----------------------------------------

    displayReversedUVCountHUD (boolean): UVシェルを部分UV統計HUDとしてヘッズアップ表示に表示します。

    -----------------------------------------

    displaySolidMap (boolean): アクティブテクスチャマップのソリッドオーバーレイを表示します。

    -----------------------------------------

    displayStyle (string): イメージを表示するモードを設定します。有効な値は、基本RGBイメージを表示する場合は「カラー」マスクチャネルを表示する場合は「マスク」イメージの輝度を表示する場合は「輝度」

    -----------------------------------------

    displayTextureBorder (boolean): テクスチャ境界の表示を切り替えます。

    -----------------------------------------

    displayUVPositionHUD (boolean): UV位置のヘッズアップ表示を表示

    -----------------------------------------

    displayUVShellCountHUD (boolean): UVシェル数を部分UV統計HUDとしてヘッズアップ表示に表示します。

    -----------------------------------------

    displayUVStatisticsHUD (boolean): UV統計のヘッズアップ表示を表示

    -----------------------------------------

    displayUsedPercentageHUD (boolean): 使用済みUV空間のパーセンテージを部分UV統計HUDとしてヘッズアップ表示に表示します。

    -----------------------------------------

    distortionAlpha (float): 歪み表示のアルファを設定または照会します。

    -----------------------------------------

    distortionPerObject (boolean): オブジェクトごとの歪み表示を切り替えます。

    -----------------------------------------

    divisions (int): メイングリッドライン間のサブディビジョン数を設定します。

    -----------------------------------------

    docTag (string): エディタにタグをアタッチします。

    -----------------------------------------

    doubleBuffer (boolean): 表示をダブルバッファモードに設定します。

    -----------------------------------------

    drawAxis (boolean): 軸が描画されるかどうかを設定または照会します。

    -----------------------------------------

    drawSubregions (boolean): サブ領域表示を切り替えます。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    exposure (float): 現在のエディタのカラー管理に使用される露出値です。

    -----------------------------------------

    filter (string): このエディタに使用する項目フィルタオブジェクトの名前を指定します。エディタの主要リストに表示される情報をフィルタします。

    -----------------------------------------

    forceMainConnection (string): エディタがコンテンツのソースとして使用するselectionConnectionオブジェクトの名前を指定します。エディタはselectionConnectionオブジェクトに含まれている項目のみを表示します。これは-mainListConnectionフラグの変形で、接続がロックされている場合でも強制的に変更します。このフラグを使用して、-unlockMainConnection、-mainListConnection、-lockMainConnectionフラグを直後に連続して使用する場合に、オーバーヘッドを減します。

    -----------------------------------------

    forceRebake (boolean): 強制的に現在のキャッシュテクスチャをリフレッシュします。

    -----------------------------------------

    frameAll (boolean): シーン全体をズームします。

    -----------------------------------------

    frameSelected (boolean): 現在選択しているオブジェクトをズームします。

    -----------------------------------------

    frontFacingColor ([float, float, float, float]): RGBAフロントフェース側のカラーを設定または照会します。

    -----------------------------------------

    gamma (float): 現在のエディタのカラー管理に使用されるガンマ値です。

    -----------------------------------------

    gridLinesColor ([float, float, float]): グリッド線の色です。既定は、0.3250.3250.325です。

    -----------------------------------------

    gridNumbersColor ([float, float, float]): グリッド番号の色です。既定は0.20.20.2です。

    -----------------------------------------

    highlightConnection (string): そのハイライトリストをエディタと同期化させるselectionConnectionオブジェクトの名前を指定します。すべてのエディタにハイライトリストがあるわけではありません。ハイライトリストがあるエディタの場合、これは第二の選択項目を表示したリストになります。

    -----------------------------------------

    imageBaseColor ([float, float, float]): イメージのベースカラー。既定は白1.01.01.0です。

    -----------------------------------------

    imageDim (boolean): イメージの淡色表示を切り替えます。

    -----------------------------------------

    imageDisplay (boolean): テクスチャイメージの表示を切り替えます。

    -----------------------------------------

    imageNames (boolean): 表示可能なすべてのテクスチャイメージの名前をリストします(存在する場合)。

    -----------------------------------------

    imageNumber (int): 表示するテクスチャイメージの番号を設定します。これは、現在選択しているテクスチャの数によって異なります。N個のテクスチャがある場合、想定されるテクスチャイメージの番号は0からN-1までとなります。

    -----------------------------------------

    imagePixelSnap (boolean): UVテクスチャエディタ内でUV変換を行うときに、UV値が画像のピクセルコーナーにスナップされるようにモードを設定します。どのピクセルが使用されるかは、テクスチャイメージまたはエディタイメージのどちらが表示されるかによって決まります。両方が表示される場合は、テクスチャイメージのピクセルが使用されます。

    -----------------------------------------

    imageRatio (boolean): テクスチャイメージの縦横比を使用して描画するようにウィンドウを設定します。幅が高さよりも大きい場合は、幅が「1ユニット」として設定され、高さは幅を高さで割って調整されます。これはテクスチャイメージの表示には影響しますが、エディタイメージには影響しません。

    -----------------------------------------

    imageRatioValue (float): UVエディタのイメージ比率の現在の値を照会します。

    -----------------------------------------

    imageSize (boolean): 現在表示されているテクスチャイメージのサイズを返します。返される値は、幅、高さの順です。これは参照のみ可能です。

    -----------------------------------------

    imageTileRange ([float, float, float, float]): 表示のUV範囲を設定します。4つの値(float)は最小U、最小V、最大U、最大Vの順で指定します。テクスチャイメージを表示する場合、これらの値は適切なパラメータ(例:繰り返しUV(RepeatUV)、ミラー(Mirror)、ラップ(Wrap)など)に基づいてイメージを何倍でタイル表示するかに影響します。エディタイメージを表示する場合、これらの値はイメージの可視サイズを決定します。たとえば、その範囲を(0,0,2,1)に設定すると、エディタイメージを2x1の四角形で、使用可能なスペースを満たすために必要に応じて変形してロードします。

    -----------------------------------------

    imageUnfiltered (boolean): テクスチャイメージをフィルタ処理しないように設定します。表示解像度が画像の解像度を上回ると、画像は「ピクセル化」した状態で表示されます。

    -----------------------------------------

    internalFaces (boolean): 選択したコンポーネントに含まれるフェースを表示します。

    -----------------------------------------

    labelPosition (string): グリッドの数字ラベルの位置です。有効な値は「axis」と「edge」です。

    -----------------------------------------

    loadImage (string): ディスクからイメージをロードして現在のエディタイメージとして設定します。

    -----------------------------------------

    lockMainConnection (boolean): mainConnection内のオブジェクトの現在のリストをロックして、そのオブジェクトだけがエディタ内に表示されるようにします。これ以降、元のmainConnectionに変更を加えても無視されます。

    -----------------------------------------

    mainListConnection (string): エディタがコンテンツのソースとして使用するselectionConnectionオブジェクトの名前を指定します。エディタはselectionConnectionオブジェクトに含まれている項目のみを表示します。

    -----------------------------------------

    maxResolution (int): このフラグは現在のキャッシュされたテクスチャの最大解像度を設定します。

    -----------------------------------------

    multiColorAlpha (float): シェーディングされたUVのマルチカラーのアルファを設定します。

    -----------------------------------------

    nbImages (boolean): イメージの数を返します。

    -----------------------------------------

    nextView (boolean): 次のビューに切り替えます。

    -----------------------------------------

    numUvSets (boolean): このフラグは、テクスチャウィンドウで選択したオブジェクトのUVセットの数を返します。

    -----------------------------------------

    numberOfImages (int): 現在表示可能なテクスチャイメージの数です。

    -----------------------------------------

    numberOfTextures (int): 現在表示可能なテクスチャの数です。

    -----------------------------------------

    panel (string): このエディタ用のパネルを指定します。既定では、エディタがスクリプトパネルの作成コールバックで作成された場合、エディタはそのパネルに属します。エディタがパネルに属していない場合、エディタのあるウィンドウを削除するとエディタも削除されます。

    -----------------------------------------

    parent (string): このエディタの親のレイアウトを指定します。このフラグは、エディタが現在ペアレント化されていない場合のみに効果があります。

    -----------------------------------------

    previousView (boolean): 前のビューに切り替えます。

    -----------------------------------------

    realSize (boolean): 画像を内部バッファのサイズとともに表示します。注:現在では、この引数はイメージ表示に影響しなくなりました。

    -----------------------------------------

    refresh (boolean): 現在のエディタイメージのリフレッシュを要求します。

    -----------------------------------------

    relatedFaces (boolean): 選択したコンポーネントに接続されたフェースを表示します。

    -----------------------------------------

    removeAllImages (boolean): エディタイメージスタックからすべてのエディタイメージを除去します。

    -----------------------------------------

    removeImage (boolean): エディタイメージスタックから現在のエディタイメージを除去します。

    -----------------------------------------

    rendererString (string): 現在のレンダラを記述する文字列を設定または照会します。

    -----------------------------------------

    reset (boolean): 地表プレーンを既定値にリセットします。

    -----------------------------------------

    saveImage (boolean): メモリに現在のEditorImageを保存します。保存されたエディタイメージは、エディタイメージスタックに格納されます。最も新しく保存したイメージは0の位置に、次に新しく保存したイメージは1の位置、などと格納されます。現在のエディタイメージを前に保存したイメージに設定するには、「di/displayImage」フラグを使用します。

    -----------------------------------------

    scaleBlue (float): ビュー内の青の成分のスケーリング係数を定義します。既定値は1で、-1000から+1000までが可能です。

    -----------------------------------------

    scaleGreen (float): ビュー内の緑の成分のスケーリング係数を定義します。既定値は1で、-1000から+1000までが可能です。

    -----------------------------------------

    scaleRed (float): ビュー内の赤の成分のスケーリング係数を定義します。既定値は1で、-1000から+1000までが可能です。

    -----------------------------------------

    selectInternalFaces (boolean): 選択したコンポーネント(内部)に含まれているフェースをselectionListに追加します。

    -----------------------------------------

    selectRelatedFaces (boolean): 選択したコンポーネント(内部は関連せず)に含まれているフェースをselectionListに追加します。

    -----------------------------------------

    selectionConnection (string): その独自のセレクションリストをエディタと同期化させるselectionConnectionオブジェクトの名前を指定します。このエディタから選択する場合、selectionConnectionオブジェクトの中から選択します。オブジェクトが変更されると、エディタが更新されて変更が反映されます。

    -----------------------------------------

    setUvSet (int): このフラグはテクスチャウィンドウで選択したオブジェクトに、現在のUVセットを設定します。

    -----------------------------------------

    singleBuffer (boolean): 表示をシングルバッファモードに設定します。

    -----------------------------------------

    size (float): グリッドのサイズを設定します。

    -----------------------------------------

    solidMap3dView (boolean): 3Dビューポートにおけるアクティブテクスチャマップのソリッドオーバーレイを表示します。

    -----------------------------------------

    solidMapColorSeed (int): シェーディングされたUVのマルチカラーのシードを設定します。

    -----------------------------------------

    solidMapPerShell (boolean): ソリッドオーバーレイをシェルごとのランダムなカラーで表示します。

    -----------------------------------------

    spacing (float): メイングリッドラインの間隔を設定します。

    -----------------------------------------

    stateString (boolean): 照会モード専用のフラグです。エディタを作成して現在のエディタの状態と一致させるMELコマンドを返します。返されたコマンド文字列は、指定した名前の代わりに文字列変数$editorNameを使用します。

    -----------------------------------------

    style (int): このフラグは廃止されているので、使用しないでください。

    -----------------------------------------

    subdivisionLinesColor ([float, float, float]): サブディビジョンラインのカラーです。既定は0.250.250.25です。

    -----------------------------------------

    textureBorder3dView (boolean): 3Dビューポートでテクスチャ境界の表示を切り替えます。

    -----------------------------------------

    textureBorderColor ([float, float, float]): テクスチャ境界の表示カラーを設定します。

    -----------------------------------------

    textureBorderWidth (int): テクスチャ境界の表示エッジの幅を設定します。

    -----------------------------------------

    textureNames (boolean): 表示可能なすべてのテクスチャイメージのテクスチャ名です(存在する場合)。

    -----------------------------------------

    textureNumber (int): 表示するテクスチャの数を設定します。これは、現在選択しているテクスチャの数によって異なります。N個のテクスチャがある場合、想定されるテクスチャイメージの番号は0からN-1までとなります。

    -----------------------------------------

    tileLabels (boolean): テクスチャタイルのラベル表示を切り替えます。

    -----------------------------------------

    tileLinesColor ([float, float, float]): タイルラインの色です。既定は0.00.00.0です。

    -----------------------------------------

    toggle (boolean): 地表プレーンの表示を切り替えます。

    -----------------------------------------

    toggleExposure (boolean): エディタの現在の露出値と既定の露出値を切り替えます。

    -----------------------------------------

    toggleGamma (boolean): エディタの現在のガンマ値と既定のガンマ値を切り替えます。

    -----------------------------------------

    unParent (boolean): エディタをそのレイアウトから除去するように指定します。これは照会モードでは使用できません。

    -----------------------------------------

    unlockMainConnection (boolean): mainConnectionをロック解除して、オリジナルのmainConnection(まだ使用可能な場合)を効率的に復元し、ダイナミックな更新を行います。

    -----------------------------------------

    updateMainConnection (boolean): ロックされたmainConnectionをオリジナルのmainConnectionから更新させますが、ロック状態は保持されます。

    -----------------------------------------

    useFaceGroup (boolean): 描画されるメッシュノードに設定されたgroupIdに関連付けれられたフェースを表示します(アトリビュート:displayFacesWithGroupId)。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    usedPercentageHUDRange ([float, float, float, float]): 使用済みUV空間のパーセンテージを計算する際の範囲を設定します。4つの値は最小U、最小V、最大U、最大Vの順で指定し、既定は0011です。

    -----------------------------------------

    uvSets (boolean): このフラグは、テクスチャウィンドウで選択したオブジェクトの、UVセットとオブジェクト名のペアを含んだ文字列を返します。各ペアの構文は「objectName|uvSetName」で、|の部分はそのままの文字です。

    -----------------------------------------

    viewPortImage (boolean): ビューポートとキャッシングテクスチャイメージを切り替えます。

    -----------------------------------------

    viewTransformName (string): 現在のエディタでカラー管理が有効になっている場合に適用されるビューパイプラインを設定します。

    -----------------------------------------

    wireframeComponentColor ([float, float, float, float]): RGBAコンポーネントワイヤフレームのカラーを設定または照会します。

    -----------------------------------------

    wireframeObjectColor ([float, float, float, float]): RGBAオブジェクトワイヤフレームのカラーを設定または照会します。

    -----------------------------------------

    writeImage (string): ディスクに現在のエディタイメージを書き込みます。

    -----------------------------------------

    Return Value:
    None: stringテクスチャ ウィンドウの名前照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def uvLink(b: bool = False,isValid: bool = False,make: bool = False,queryObject: str = "",texture: str = "",uvSet: str = "") -> None:
    """
    オブジェクトの UV セットとその UV セットで使用されるテクスチャ間で、UV のリンク機能リレーションの作成、切断、照会を行うのに使用します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    b (boolean): コマンドでこのフラグを指定すると、UVセットとテクスチャ間のリンクを切断するためにコマンドが呼び出されます。

    -----------------------------------------

    isValid (boolean): このフラグを使用して、テクスチャまたはUVセットがUVリンクに有効かどうかを検証します。これは-textureフラグまたは-uvSetフラグとともに使用されますが、両方のフラグを一度には使うことはできません。

    -----------------------------------------

    make (boolean): コマンドでこのフラグを指定すると、UVセットとテクスチャの間にリンクを作成するためにコマンドが呼び出されます。

    -----------------------------------------

    queryObject (name): このフラグはテクスチャの照会時のみに使われます。このフラグを使用して、照会結果がこのフラグで指定したオブジェクトのUVセットに限定されることを示します。

    -----------------------------------------

    texture (name): textureフラグの引数は、アクションの実行時にコマンドが使用するテクスチャを指定します。

    -----------------------------------------

    uvSet (name): uvSetフラグの引数は、アクションの実行時にコマンドが使用するUVセットを指定します。

    -----------------------------------------

    Return Value:
    None: stringまたは、isValid の照会ブーリアンの文字配列です。照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def vectorize(browserView: bool = False,byFrame: float = 1.0,camera: str = "",combineFillsEdges: bool = False,currentFrame: bool = False,curveTolerance: float = 1.0,customExtension: str = "",detailLevel: int = 1,edgeColor: Tuple[int, int, int] = tuple(1, 1, 1),edgeDetail: bool = False,edgeStyle: str = "",edgeWeight: float = 1.0,endFrame: float = 1.0,filenameFormat: str = "",fillStyle: str = "",flashVersion: int = 1,frameRate: int = 1,height: int = 1,hiddenEdges: bool = False,highlightLevel: int = 1,highlights: bool = False,imageFormat: str = "",layer: str = "",minEdgeAngle: float = 1.0,outlinesAtIntersections: bool = False,outputFileName: str = "",pixelAspectRatio: float = 1.0,reflectionDepth: int = 1,reflections: bool = False,renderLayers: bool = False,renderOptimization: str = "",renderView: bool = False,secondaryCurveFitting: bool = False,shadows: bool = False,showBackFaces: bool = False,startFrame: float = 1.0,svgAnimation: str = "",svgCompression: bool = False,width: int = 1) -> None:
    """
    このコマンドでは、Maya ベクター レンダラを使用して、Maya シーンを各種のベクター フォーマットやラスター フォーマットにレンダーします。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    browserView (boolean): レンダーをブラウザでプレビューするかどうかを指定します。このオプションはswfのみです。

    -----------------------------------------

    byFrame (float): フレーム増分を指定します。

    -----------------------------------------

    camera (string): レンダーするカメラを指定します。

    -----------------------------------------

    combineFillsEdges (boolean): Flashで、フィルまたはエッジを単一のオブジェクトとして結合するかどうかを指定します。このオプションはswfのみです。

    -----------------------------------------

    currentFrame (boolean): 現在のフレームのみをレンダーするかどうかを指定します。

    -----------------------------------------

    curveTolerance (float): カーブ許容値を指定します。有効な値は、0.0～15.0です。カーブ許容値によって、接続された一連のラインセグメントを、レンダラがどのくらいアグレッシブにカーブに合わせようとするかが定義されます。値0.0では、すべてのラインセグメントがカーブフィッティングなしで描画されます。値15.0では、アグレッシブなカーブフィッティングが発生します。

    -----------------------------------------

    customExtension (string): ファイル名に使用するカスタム拡張子を指定します。空でない任意の文字列が有効です。

    -----------------------------------------

    detailLevel (int): 詳細レベルを指定します。有効な値は、0～50です。値が小さいほど、多くのポリゴンが結合可能になり、小さなファイルが生成されます。大きな値では、レンダーの正確さが高まりますが、ファイルサイズが大きくなり、レンダー時間が長くなります。

    -----------------------------------------

    edgeColor ([int, int, int]): エッジカラーの赤、緑、青の成分を指定します。有効な値は、各カラー成分に対して0～255です。

    -----------------------------------------

    edgeDetail (boolean): エッジの詳細をレンダーするかどうかを指定します。これは、1つのエッジを共有する任意の2つの隣接ポリゴンのフェース法線間の角度が、(-meaフラグによって指定される)最小エッジ角度より大きなエッジです。

    -----------------------------------------

    edgeStyle (string): エッジスタイルを指定します。有効な値は、「Outline」、「EntireMesh」、「None」です。

    -----------------------------------------

    edgeWeight (float): すべてのエッジの入力ポイントに使用するエッジウェイトを指定します。1インチあたり72のポイントがあります。値0.0は、極細(Hairline)エッジウェイトを指定します。

    -----------------------------------------

    endFrame (float): 終了フレームを指定します。

    -----------------------------------------

    filenameFormat (string): ファイル名フォーマットを指定します。有効な値は、「name」、「name.ext」、「name.#.ext」、「name.ext.#」、「name.#」、「name#.ext」、「name_#.ext」です。

    -----------------------------------------

    fillStyle (string): 塗り潰しスタイルを指定します。有効な値は、「SingleColor」、「TwoColor」、「FourColor」、「FullColor」、「AverageColor」、「AreaGradient」、「MeshGradient」、「None」です。AreaGradientとMeshGradientは、epsおよびaiイメージフォーマットでは使用できません。

    -----------------------------------------

    flashVersion (int): swf出力のFlashバージョンを指定します。有効な値は、3、4、5です。このオプションはswfのみです。

    -----------------------------------------

    frameRate (int): フレームレートを指定します。このオプションは、svgとswfのみです。

    -----------------------------------------

    height (int): 出力イメージの高さを、ピクセル単位で指定します。

    -----------------------------------------

    hiddenEdges (boolean): 非表示エッジをレンダーするかどうかを指定します。これは、カメラから見えないエッジです。

    -----------------------------------------

    highlightLevel (int): ハイライトレベルを指定します。有効な値は、1～8です。この値は、オブジェクトのハイライトをレンダーするために使用する同心円の数を指定します。このオプションは、SingleColor、AverageColor、AreaGradient塗り潰しスタイルのみに使用します。

    -----------------------------------------

    highlights (boolean): ハイライトをレンダーするかどうかを指定します。このオプションはai、eps、svgには影響しません。このオプションは、SingleColor、AverageColor、AreaGradient塗り潰しスタイルのみに使用します。

    -----------------------------------------

    imageFormat (string): レンダーするイメージ形式を指定します。WindowsおよびMacプラットフォームで有効な値は、「swf」、「eps」、「ai」、「svg」、「jpg」、「iff」、「sgi」、「tga」、「tif」、「bmp」です。Windowsの場合に追加で有効な値は、「als」、「cin」、「gif」、「yuv」、「rla」、「si」です。Macの場合に追加で有効な値は、「pntg」、「ps」、「png」、「pict」、「qtif」、「qt」です。

    -----------------------------------------

    layer (name): 指定したレンダーレイヤをレンダーします。レンダーレイヤのレンダリング可能なアトリビュート値にかかわらず、このレンダーレイヤのみをレンダーします。レイヤ名は出力イメージファイル名にアペンドされます。指定したレンダーレイヤは、レンダリング前に現在のレンダーレイヤになり、レンダリング後も現在のレンダーレイヤのままです。

    -----------------------------------------

    minEdgeAngle (float): 最小エッジ角度を、度単位で指定します。有効な値は、0.0～90.0です。これは、-edフラグを指定したときにエッジがレンダリングされたかどうかを調べるのに使用される、2つの隣接ポリゴンのフェース法線間の最小角度です。

    -----------------------------------------

    outlinesAtIntersections (boolean): 2つのポリゴンがインターセクトするときにエッジを描画するかどうかを指定します。既定ではこのフラグは有効です。

    -----------------------------------------

    outputFileName (string): 出力ファイル名を指定します。

    -----------------------------------------

    pixelAspectRatio (float): ピクセルアスペクト比を指定します。

    -----------------------------------------

    reflectionDepth (int): 反射深度を指定します。有効な値は、1～4です。この値は、適用する反射のレベルを指定します。このオプションはai、eps、svgには影響しません。

    -----------------------------------------

    reflections (boolean): 反射をレンダーするかどうかを指定します。このオプションはai、eps、svgには影響しません。

    -----------------------------------------

    renderLayers (boolean): レンダーレイヤを独立したファイルとしてレンダーするかどうかを指定します。

    -----------------------------------------

    renderOptimization (string): レンダーの最適化を指定します。有効な値は、「無難」、「良好」、「強引」です。「無難」は冗長なジオメトリを除去します。「良好」は冗長なジオメトリと共に、高ディテール領域にズームインしないと見えないサブピクセルジオメトリも除去します。「強引」は「良好」が除去するすべてのジオメトリと共に、単一ピクセルレベルより少し上のジオメトリも除去し、影響のある領域にズームインしなくても、除去されたジオメトリを目視で検出できるようにします。

    -----------------------------------------

    renderView (boolean): レンダリングイメージをレンダービューに表示するかどうかを指定します。このオプションは、バッチレンダリング時は適用されません。

    -----------------------------------------

    secondaryCurveFitting (boolean): 二次カーブフィッティングを行うかどうかを指定します。

    -----------------------------------------

    shadows (boolean): シャドウをレンダーするかどうかを指定します。このオプションはai、eps、svgには影響しません。

    -----------------------------------------

    showBackFaces (boolean): バックフェースをレンダーするかどうかを指定します。これは、法線がカメラから遠ざかる方向に向いているフェースです。

    -----------------------------------------

    startFrame (float): 開始フレームを指定します。

    -----------------------------------------

    svgAnimation (string): SVGアニメーションタイプを指定します。有効な値は、「Native」、「HTMLScript」です。このオプションはSVGのみです。

    -----------------------------------------

    svgCompression (boolean): SVG出力を圧縮するかどうかを指定します。このオプションはSVGのみです。

    -----------------------------------------

    width (int): 出力イメージの幅を、ピクセル単位で指定します。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def camera(aspectRatio: float = 1.0,cameraScale: float = 1.0,centerOfInterest: float = 1.0,clippingPlanes: bool = False,depthOfField: bool = False,displayFieldChart: bool = False,displayFilmGate: bool = False,displayFilmOrigin: bool = False,displayFilmPivot: bool = False,displayGateMask: bool = False,displayResolution: bool = False,displaySafeAction: bool = False,displaySafeTitle: bool = False,fStop: float = 1.0,farClipPlane: float = 1.0,farFocusDistance: float = 1.0,filmFit: str = "",filmFitOffset: float = 1.0,filmRollOrder: str = "",filmRollValue: float = 1.0,filmTranslateH: float = 1.0,filmTranslateV: float = 1.0,focalLength: float = 1.0,focusDistance: float = 1.0,homeCommand: str = "",horizontalFieldOfView: float = 1.0,horizontalFilmAperture: float = 1.0,horizontalFilmOffset: float = 1.0,horizontalPan: float = 1.0,horizontalRollPivot: float = 1.0,horizontalShake: float = 1.0,journalCommand: bool = False,lensSqueezeRatio: float = 1.0,lockTransform: bool = False,motionBlur: bool = False,name: str = "",nearClipPlane: float = 1.0,nearFocusDistance: float = 1.0,orthographic: bool = False,orthographicWidth: float = 1.0,overscan: float = 1.0,panZoomEnabled: bool = False,position: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),postScale: float = 1.0,preScale: float = 1.0,renderPanZoom: bool = False,rotation: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),shakeEnabled: bool = False,shakeOverscan: float = 1.0,shakeOverscanEnabled: bool = False,shutterAngle: float = 1.0,startupCamera: bool = False,stereoHorizontalImageTranslate: float = 1.0,stereoHorizontalImageTranslateEnabled: bool = False,verticalFieldOfView: float = 1.0,verticalFilmAperture: float = 1.0,verticalFilmOffset: float = 1.0,verticalLock: bool = False,verticalPan: float = 1.0,verticalRollPivot: float = 1.0,verticalShake: float = 1.0,worldCenterOfInterest: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),worldUp: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),zoom: float = 1.0) -> None:
    """
    指定したプロパティでカメラを作成、編集、または照会します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    aspectRatio (float): フィルムバックの幅と高さの比率を設定します。

    -----------------------------------------

    cameraScale (float): カメラをスケールします。

    -----------------------------------------

    centerOfInterest (linear): カメラの視点から注視点までの直線距離を設定します。

    -----------------------------------------

    clippingPlanes (boolean): 手動でクリッピングプレーンを有効にします。

    -----------------------------------------

    depthOfField (boolean): オブジェクトの距離によって異なる焦点を設定するために、フィールド深度の計算を実行するかどうかを決定します。

    -----------------------------------------

    displayFieldChart (boolean): カメラで見ているときの、ビデオのフィールドチャートの表示を有効にします。

    -----------------------------------------

    displayFilmGate (boolean): カメラで見ているときの、フィルムゲートアイコンの表示を有効にします。

    -----------------------------------------

    displayFilmOrigin (boolean): カメラで見ているときの、フィルム原点のガイド表示を有効にします。

    -----------------------------------------

    displayFilmPivot (boolean): カメラで見ているときの、フィルムピボットのガイド表示を有効にします。

    -----------------------------------------

    displayGateMask (boolean): ゲートマスク、ファイル、または解像度を、ビューポートのエッジに向けてシェーディングされた領域として表示します。

    -----------------------------------------

    displayResolution (boolean): カメラで見るときの、現在のレンダー解像度(レンダーグローバル(RenderGlobals)で定義された)の表示を有効にします。

    -----------------------------------------

    displaySafeAction (boolean): カメラで見るときの、ビデオのセーフアクションのガイド表示を有効にします。

    -----------------------------------------

    displaySafeTitle (boolean): カメラで見るときの、ビデオのセーフタイトルのガイド表示を有効にします。

    -----------------------------------------

    fStop (float): 実際のレンズには通常、レンズを通過する光を遮るダイヤフラムまたは他の絞りがあります。通常この絞りはほぼ円形で、レンズの正面から見たその直径がレンズの径と呼ばれています。レンズの径はしばしばレンズの焦点距離との関係によって定義されています。レンズの径が焦点距離の1/8であるレンズは、絞り(F)値8と呼ばれます。これは、レンズの光学的な性質です。

    -----------------------------------------

    farClipPlane (linear): ファークリッピングプレーンまでの距離を指定します。

    -----------------------------------------

    farFocusDistance (linear): ファー焦点(近距離)プレーンまでの直線距離を設定します。

    -----------------------------------------

    filmFit (string): どのようにデジタルイメージ(ピクセル単位)とフィルムバックを適合させるかを指定します。フィルムバックでは任意のフィルムのアスペクトが実数で定義され、デジタルイメージでは同等の任意の(しかし異なる)解像度が整数ピクセルで定義されるので、この2つを適合させるのはかなり複雑になります。デジタルイメージとフィルムバックを適合させるには、次の4つの選択肢があります。horizontalこの場合、デジタルイメージは、水平方向でフィルムバックにぴったり一致するように変更されます。各ピクセルの水平方向のサイズ=(フィルムバック幅)/(水平解像度)になります。したがって、ピクセルの高さ=(ピクセルの幅)/(ピクセルアスペクト比)になります。ピクセルにはサイズがあるので、解像度により完全なイメージが得られます。そのイメージは、フィルムバックの幅と正確に一致します。高さについては、高すぎたり低すぎたりしてほとんど一致することはありません。ただし、数字を調整することで、非常に近い高さにすることはできます。vertical考え方は水平フィットと同じですが、垂直方向に適用されます。よって、デジタルイメージの高さはフィルムバックにぴったり一致しますが、幅は一致しません。fillこれは便利な項目です。システムは、水平フィットと垂直フィットの両方を計算し、デジタルイメージがフィルムバックより大きくなる方を適用します。overscanカメラビューでフィルムゲートをオーバースキャンすると、ドリーやズームに頼らずに、カメラビュー内からフラスタムの外側の振り付けアクションを行えます。この機能も、イメージプレーンをアニメートするために不可欠です。

    -----------------------------------------

    filmFitOffset (float): 上記の説明からわかるように、デジタルイメージがフィルムバックと正確に一致しないことがあるので、デジタルイメージとフィルムバックとの位置をどのように合わせるかという問題が残ります。このような場合、filmFitOffsetが役に立ちます。通常、センターは位置合わせされています。filmFitOffsetにより、小さな方のイメージを大きなイメージの中に移動します。フィルムのオフセット距離をインチで指定します。

    -----------------------------------------

    filmRollOrder (string): ピボット値との関係でどのように回転を適用するかを指定します。Rotate-Translateフィルムバックを最初に回転し、ピボットポイントの値分、移動します。Translate-Rotateフィルムバックを最初に移動し、ピボットロールの値分、移動します。

    -----------------------------------------

    filmRollValue (angle): フィルムバックの回転量を指定します。回転値は度単位で指定します。回転は、指定されたピボットポイントを中心に行われます。この値は、ポスト投影マトリックスの成分で、フィルムロールマトリックスの計算に使用されます。

    -----------------------------------------

    filmTranslateH (float): フィルムの水平方向の移動です。値は表示領域に対して正規化されます。

    -----------------------------------------

    filmTranslateV (float): フィルムの垂直方向の移動です。値は表示領域に対して正規化されます。

    -----------------------------------------

    focalLength (float): 「焦点距離」が無限大になったときの、レンズとフィルムプレーンの間のレンズ軸に沿った距離です。これは、レンズの光学的な性質です。この倍精度パラメータは、常にミリメートル(mm)単位で指定します。

    -----------------------------------------

    focusDistance (linear): カメラ正面の一定の距離に焦点を設定します。

    -----------------------------------------

    homeCommand (string): 「viewSet-home」がこのカメラに適用された場合に実行するコマンドを指定します。すべての「%camera」パラメータは、viewSetがコマンドを実行する前にカメラ名に置き換えられます。

    -----------------------------------------

    horizontalFieldOfView (angle): これは、無限大に焦点を合わせた(つまり、焦点距離が遠くにある)場合にレンズから見たフィルムバックの幅で、角度として測定されます。測定された角度は、ピクセル、デジタルイメージ、またはどのアスペクトにも関係しないことに注意してください。ビューアングルは派生フィールドで、Aliasによって内部的に使用されず、他の情報で完全に定義することができます。ユーザの便宜のために用意されています。ビューアングルは、aov=2×atan(fbw/(2×f))の式で導かれます。ここで、「aov」はビューアングル、「fbw」は再生フィルム幅、「f」は焦点距離です。

    -----------------------------------------

    horizontalFilmAperture (float): カメラのフィルムプレーンの水平方向の幅です。カメラのフィルムは、フィルムプレーンに配置されています。レンズ正面のシーンのイメージに対して露出されているフィルムの大きさで、フィルムバックの長方形の領域に制限されます。この倍精度パラメータは、常にインチ(inch)で指定します。

    -----------------------------------------

    horizontalFilmOffset (float): フィルムバックの中心からの水平方向のオフセットです。通常、フィルムバックはレンズ軸上にセンタリングされます。しかし、これは必ずしもそうだというわけではありません。フィルムオフセットは、レンズ軸からのフィルムバックの中心のディスプレイスメントで、インチ(inch)で測定されます。フィルムバックをオフセットするとイメージが歪むので注意してください。焦点は変わりません。この倍精度パラメータは、常にインチ(inch)で指定します。

    -----------------------------------------

    horizontalPan (float): カメラの水平2Dパン(インチ)

    -----------------------------------------

    horizontalRollPivot (float): 再生フィルムの中心からの水平ピボットポイント。このピボットポイントは、再生フィルムの回転中に使用されます。ピボットは、回転の中心となるポイントです。この倍精度パラメータは、正規化されたビューポートに対応します。この値は、投影後のマトリックスの一部になります。

    -----------------------------------------

    horizontalShake (float): フィルムバックの中心からの別の水平オフセットです。水平フィルムオフセットアトリビュートに加えてカメラ上で使用することや格納することができます。カメラ内部でのフィルムベースのカメラシェイクを可能にします。これは、フィルムオフセットアトリビュートとまったく同じ単位と座標で機能します。このアトリビュートのエフェクトは、シェイクの有効化アトリビュートによって切り替えられます。

    -----------------------------------------

    journalCommand (boolean): Journalコマンドはcameraコマンドとインタラクティブに作用します。カメラがジャーナルされる場合、コマンドは元に戻すことができます。

    -----------------------------------------

    lensSqueezeRatio (float): 現在のところ、これはカメラエディタの情報フィールドにすぎませんが、一部のフィルムフォーマットで通常使用されているアナモフィックレンズの水平方向のゆがみを矯正することを目的としています。このフラグを使用した場合、ピクセルアスペクトのような働きをします。ただし、レンズの歪み(意図的であろうと、なかろうと)は出力ハードウェアの量子化とはわずかに異なることに注意してください。「net」の歪みパラメータは両方に対して使用できるため、混乱を招く可能性があります。

    -----------------------------------------

    lockTransform (boolean): カメラをロックします。カメラがロックされた場合、トランスフォーム情報、つまり移動(Translate)および回転(Rotate)プロパティを調整することはできず、注視点は移動できません。正投影カメラでは、正投影幅(OrthographicWidth)もロックされます。カメラグループでは、エイム(Aim)およびアップ(Up)のロケータの移動もロックされます。立体視カメラでは、ルートカメラがロックされます。

    -----------------------------------------

    motionBlur (boolean): カメラのイメージを、オブジェクトのイメージに対してモーションブラーするかどうか決定します。たとえば、カメラの動きをぼやけさせたい場合は、flybyを実行します。

    -----------------------------------------

    name (string): カメラの名前です。

    -----------------------------------------

    nearClipPlane (linear): ニアクリッピングプレーンまでの距離を指定します。

    -----------------------------------------

    nearFocusDistance (linear): ニア焦点(近距離)プレーンまでの直線距離です。

    -----------------------------------------

    orthographic (boolean): 正射投影カメラを有効にします。

    -----------------------------------------

    orthographicWidth (linear): 正射投影カメラの幅を設定します。

    -----------------------------------------

    overscan (float): オーバースキャンの値をパーセンテージで設定します。

    -----------------------------------------

    panZoomEnabled (boolean): カメラの2Dパン/2Dズームの切り替え

    -----------------------------------------

    position ([linear, linear, linear]): カメラを移動させるための3つのリニア値を指定できます。

    -----------------------------------------

    postScale (float): スケール後の値です。計算した投影マトリックスに対してこの値が掛けられます。フィルムロール後に適用されます。

    -----------------------------------------

    preScale (float): スケール前の値です。計算した投影マトリックスに対してこの値が掛けられます。フィルムロール前に適用されます。

    -----------------------------------------

    renderPanZoom (boolean): レンダーでのカメラの2Dパン/2Dズームの切り替え

    -----------------------------------------

    rotation ([angle, angle, angle]): カメラを回転させるための3つの角度値を指定できます。

    -----------------------------------------

    shakeEnabled (boolean): 水平と垂直シェイクアトリビュートのエフェクトを切り替えます。

    -----------------------------------------

    shakeOverscan (float): 出力レンダリングイメージのオーバースキャンの量をコントロールします。フィルムベースのカメラシェイクを追加するために使用します。カメラのフィルムアパーチャへの乗数として機能します。

    -----------------------------------------

    shakeOverscanEnabled (boolean): オーバースキャンのシェイクアトリビュートのエフェクトを切り替えます。

    -----------------------------------------

    shutterAngle (angle): シャッター角度(度)を指定します。

    -----------------------------------------

    startupCamera (boolean): スタートアップカメラに削除不能の暗黙のフラグを付けます。このフラグは、カメラのスタートアップ状態を設定または照会するために使用できます。スタートアップカメラは、常に最低1つ設定する必要があります。

    -----------------------------------------

    stereoHorizontalImageTranslate (float): 立体視カメラリグで使用するためのフィルムバックオフセットです。

    -----------------------------------------

    stereoHorizontalImageTranslateEnabled (boolean): 立体視HITアトリビュートのエフェクトを切り替えます。

    -----------------------------------------

    verticalFieldOfView (angle): ビューの垂直方向のフィールドを設定します。

    -----------------------------------------

    verticalFilmAperture (float): カメラのフィルムプレーンの垂直方向の高さです。この倍精度パラメータは、常にインチ(inch)で指定します。

    -----------------------------------------

    verticalFilmOffset (float): フィルムバックの中心からの垂直方向のオフセットです。この倍精度パラメータは、常にインチ(inch)で指定します。

    -----------------------------------------

    verticalLock (boolean): 垂直フィルムアパーチャのサイズをロックします。

    -----------------------------------------

    verticalPan (float): カメラの垂直2Dパン(インチ)

    -----------------------------------------

    verticalRollPivot (float): フィルムバックの回転に使用する垂直方向のピボットポイントです。この倍精度パラメータは、正規化されたビューポートに対応します。この値を使用して、投影後のマトリックスの成分である、フィルムロールマトリックスが計算されます。

    -----------------------------------------

    verticalShake (float): フィルムバックの中心からの垂直方向のオフセットです。水平シェイクアトリビュートの説明を参照してください。この項目は、シェイクの有効化アトリビュートによって切り替えられます。

    -----------------------------------------

    worldCenterOfInterest ([linear, linear, linear]): カメラのワールド座標での注視点です。

    -----------------------------------------

    worldUp ([linear, linear, linear]): カメラのワールドアップベクトルの座標です。

    -----------------------------------------

    zoom (float): フィルムで表示可能なフラスタムを表示する割り合い

    -----------------------------------------

    Return Value:
    None: string[](トランスフォーム名とシェイプ名)照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def cameraSet(active: bool = False,appendTo: bool = False,camera: str = "",clearDepth: bool = False,deleteAll: bool = False,deleteLayer: bool = False,insertAt: bool = False,layer: int = 1,name: str = "",numLayers: bool = False,objectSet: str = "",order: int = 1) -> None:
    """
    このコマンドは、カメラ セット ノードを管理します。カメラ セットを使用すると、1 つのカメラ ショットを複数のレイヤに分けることができます。1 つのカメラですべてのオブジェクトを描くのではなく、カメラを分離して特定のオブジェクトに焦点を絞ることや、他のオブジェクトを描くビューポートに別のカメラをレイヤ化することができます。主に立体シーンを構築するときに使用されるカメラ セットです。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    active (boolean): アクティブカメラレイヤを取得/設定します。

    -----------------------------------------

    appendTo (boolean): cameraSetレイヤリストの最後に新しいカメラおよび/またはオブジェクトセットをアペンドします。このフラグは、insertフラグと一緒に使用できません。また、cameraおよび/またはobjectSetフラグを使用する必要があります。

    -----------------------------------------

    camera (string): 特定レイヤのcameraを設定/取得します。照会モードでは、layerフラグを使用してレイヤを指定する必要があります。

    -----------------------------------------

    clearDepth (boolean): レイヤに描画する前に描画バッファをクリアするかどうかを指定します

    -----------------------------------------

    deleteAll (boolean): すべてのカメラレイヤを削除します

    -----------------------------------------

    deleteLayer (boolean): カメラセットからレイヤを削除します。layerフラグを使用してレイヤを指定する必要があります。

    -----------------------------------------

    insertAt (boolean): 指定したカメラおよび/またはオブジェクトセットを指定したレイヤに挿入します。このフラグはappendフラグと一緒に使用することはできません。また、layerおよびcamera(またはobjectSet)フラグを使用する必要があります。

    -----------------------------------------

    layer (int): レイヤ情報にアクセスする際に使用するレイヤインデックスを指定します

    -----------------------------------------

    name (string): 作成したカメラセットの名前を取得または設定します。

    -----------------------------------------

    numLayers (boolean): 指定したcameraSetに定義されたレイヤ数を返します

    -----------------------------------------

    objectSet (string): 特定レイヤのobjectSetを設定/取得します。照会モードでは、layerフラグを使用してレイヤを指定する必要があります。

    -----------------------------------------

    order (int): 特定レイヤを処理する順序を設定します。このフラグはlayerフラグと一緒に使用する必要があります。

    -----------------------------------------

    Return Value:
    None: string新しい cameraSet ノード(作成モード時)照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def cameraView(addBookmark: bool = False,animate: bool = False,bookmarkType: int = 1,camera: str = "",name: str = "",removeBookmark: bool = False,setCamera: bool = False,setView: bool = False) -> None:
    """
    このコマンドは、カメラから独立しているカメラのプリセット ビューを作成します。ビューは、カメラの視点、注視点、アップ ベクトル、タンブルのピボット、水平アパーチャ、垂直アパーチャ、焦点距離、正射投影幅、そしてカメラの既定のビューが正射投影かパース ビューかなどの情報を格納します。2D パン/ズーム アトリビュートを格納するには、bookmarkType を 1 に設定する必要があります。この設定は、set camera フラグで、他の任意のカメラに適用することができます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    addBookmark (boolean): このビューを指定したカメラ、またはアクティブなモデルパネルのカメラに関連付けます。このフラグは、作成または編集に使用することができます。

    -----------------------------------------

    animate (boolean): ビューの切り替えにアニメーション機能を設定します。

    -----------------------------------------

    bookmarkType (int): ブックマークタイプを次の選択肢から指定します。0.3Dブックマーク。1.2Dパン/ズームブックマーク

    -----------------------------------------

    camera (name): 使用するカメラを指定します。このフラグはaddbookmark、removebookmark、setcamera、またはsetviewflagsのいずれかと一緒に使用する必要があります。このフラグが指定されていない場合、アクティブなモデルパネルのカメラが使用されます。

    -----------------------------------------

    name (string): ビューの名前を設定します。このフラグは作成にのみ使用できます。

    -----------------------------------------

    removeBookmark (boolean): このビューと指定したカメラまたはアクティブなモデルパネルのカメラとの関連付けを除去します。これは、編集でのみ使用できます。

    -----------------------------------------

    setCamera (boolean): このビューをcameraフラグまたはアクティブなモデルパネルのカメラで指定したカメラに設定します。このフラグは編集にのみ使用できます。

    -----------------------------------------

    setView (boolean): カメラビューを指定したカメラまたはアクティブなモデルパネルに合わせて設定します。このフラグは編集にのみ使用できます。

    -----------------------------------------

    Return Value:
    None: string(カメラ ビュー名)
    """
    pass

    
def dolly(absolute: bool = False,distance: float = 1.0,dollyTowardsCenter: bool = False,orthoScale: float = 1.0,relative: bool = False) -> None:
    """
    ワールド空間で表示方向にそってカメラが移動します。カメラの表示方向とアップ方向は変化しません。操作には次の 2 つのモードがあります。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    absolute (boolean): distanceフラグとorthoScaleフラグの動作が修正されます。distanceフラグと一緒に使用する場合、distance引数は、カメラの視野の中心からカメラの視点の距離を指定します。orthoScaleフラグと一緒に使用する場合、orthoScale引数はカメラの新しい正射投影幅を指定します。

    -----------------------------------------

    distance (linear): パースビューカメラをドリーする単位距離。

    -----------------------------------------

    dollyTowardsCenter (boolean): このフラグは、ドリーがビューの中央に向かって実行される(tureの場合)のか、ユーザがクリックしたポイントに向かって実行される(falseの場合)のかを制御します。既定では、dollyTowardsCenterがオンになります。

    -----------------------------------------

    orthoScale (float): 正投影カメラの正投影幅を変更するスケール。

    -----------------------------------------

    relative (boolean): distanceフラグとorthoScaleフラグの動作が修正されます。distanceフラグと一緒に使用する場合、カメラの視点と視野の中心の両方は、distanceフラグの引数で指定する距離だけ移動します。orthoScaleフラグと一緒に使用すると、orthoScale引数はカメラの正射投影幅にかけられます。relativeフラグは既定で常にオンになっています。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def imagePlane(camera: str = "",counter: bool = False,detach: bool = False,dropFrame: bool = False,fileName: str = "",frameDuration: int = 1,height: float = 1.0,imageSize: Tuple[int, int] = tuple(1, 1),lookThrough: str = "",maintainRatio: bool = False,name: str = "",negTimesOK: bool = False,numFrames: int = 1,quickTime: bool = False,showInAllViews: bool = False,timeCode: int = 1,timeCodeTrack: bool = False,timeScale: int = 1,twentyFourHourMax: bool = False,width: float = 1.0) -> None:
    """
    imagePlane コマンドを使用すると、1 つのイメージ プレーンのさまざまなプロパティ、およびそのイメージ プレーンが使用しているムービーに対して、照会を実行できます。このコマンドは、作成と編集もサポートしています。このコマンドには、imagePlane ノードまたはカメラのいずれかのオブジェクトを渡すことができます。カメラを渡した場合は、カメラにアタッチされたイメージ プレーン(存在する場合)が使用されます。オブジェクトを渡さない場合は、現在の選択範囲が使用されます。現在、ほとんどのムービー関連の照会は、64 ビット Windows システム上でのみ機能します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    camera (string): 作成時は、指定したカメラへの作成済みイメージプレーンのアタッチを試みます。指定のカメラが無効な場合、作成は失敗します。照会時は、現在のイメージプレーンがどのカメラにアタッチされているかを照会します。(フリーイメージプレーンに)アタッチされているカメラがない場合は、空の文字列が返されます。編集時は、イメージプレーンを指定の新しいカメラにアタッチします。指定のカメラが無効な場合は、何も行われません。イメージプレーンをカメラにアタッチすると、イメージプレーンのトランスフォームノードも同一の設定になります。デタッチコマンドはイメージプレーンの元の位置を復元しません。ただし、元に戻すコマンドはイメージプレーンの元の位置を復元します。

    -----------------------------------------

    counter (boolean): ムービーのタイムコードフォーマットの「counter」フラグを照会します。これがtrueの場合、-timeCodeフラグによって返されるタイムコードは単純なカウンタです。falseの場合、返されるタイムコードは整数の配列(時間、分、秒、フレーム)です。

    -----------------------------------------

    detach (boolean): このフラグを使用できるのは編集モードの場合のみです。編集でこのフラグを使用すると、現在のイメージプレーンを、アタッチされているすべてのカメラからデタッチして、フリーのイメージプレーンにします。

    -----------------------------------------

    dropFrame (boolean): ムービーのタイムコードフォーマットの「dropframe」フラグを照会します。

    -----------------------------------------

    fileName (string): 読み込むイメージプレーンのイメージ名を設定します。

    -----------------------------------------

    frameDuration (int): ムービーのタイムコードフォーマットのフレーム期間を照会します。

    -----------------------------------------

    height (float): イメージプレーンの高さ。作成時にこのフラグが指定されていない場合、既定の高さとして10.0が使用されます。

    -----------------------------------------

    imageSize ([int, int]): ロードされたイメージのサイズを取得します。

    -----------------------------------------

    lookThrough (string): イメージプレーンを見るために現在使用されているカメラです。

    -----------------------------------------

    maintainRatio (boolean): イメージプレーンにイメージのアスペクト比を維持させます。作成時にこのフラグが指定されていない場合、既定値としてtrueが使用されます。

    -----------------------------------------

    name (string): 作成時はイメージプレーンのノード名を設定します。照会時はイメージプレーン名を返します。

    -----------------------------------------

    negTimesOK (boolean): ムービーのタイムコードフォーマットの「negtimesOK」フラグを照会します。

    -----------------------------------------

    numFrames (int): ムービーのタイムコードフォーマットの1秒あたりの全フレーム数を照会します。

    -----------------------------------------

    quickTime (boolean): イメージプレーンでQuickTimeムービーが使用されているかどうかを照会します。

    -----------------------------------------

    showInAllViews (boolean): このフラグは、現在のイメージプレーンをすべてのビューに表示するかしないかを示すために使用されます。

    -----------------------------------------

    timeCode (int): ムービーのタイムコードフォーマットの1秒あたりの全フレーム数を照会します。

    -----------------------------------------

    timeCodeTrack (boolean): イメージプレーン上のムービーにタイムコードトラックがあるかどうかを照会します。

    -----------------------------------------

    timeScale (int): ムービーのタイムコードフォーマットのタイムスケールを照会します。

    -----------------------------------------

    twentyFourHourMax (boolean): ムービーのタイムコードフォーマットの「24hourmax」フラグを照会します。

    -----------------------------------------

    width (float): イメージプレーンの幅。作成時にこのフラグが指定されていない場合、既定の幅として10.0が使用されます。

    -----------------------------------------

    Return Value:
    None: booleanコマンドの結果照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def listCameras(orthographic: bool = False,perspective: bool = False) -> None:
    """
    すべてのカメラがリストされます。フラグを指定しないと、パースビュー カメラと正投影カメラの両方が表示されます。このコマンドでは、カメラ名の配列が返されます。トランスフォーム名で、その名前が使われているカメラが固有に識別されると、それ以外の場合はシェイプの名前を返します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    orthographic (boolean): すべての正投影カメラが表示されます。

    -----------------------------------------

    perspective (boolean): すべてのパースビューカメラが表示されます。

    -----------------------------------------

    Return Value:
    None: string[]コマンドの結果
    """
    pass

    
def lookThru(farClip: float = 1.0,nearClip: float = 1.0) -> None:
    """
    ビューを見通す特定のカメラが設定されます。ライトやその他の DAG オブジェクトの負の Z 軸を表示するためにも使用できます。その場合は、標準カメラ ツールを使用してオブジェクトを配置します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    farClip (float): クリップファープレーンを新規の見通すカメラとして設定する場合に使用されます。既存のカメラのアトリビュートには影響しません。クリップ値はシェイプまたはビューの前にくる必要があります。

    -----------------------------------------

    nearClip (float): ニアクリッププレーンを新規の見通すカメラとして設定する場合に使用されます。既存のカメラのアトリビュートには影響しません。クリップ値はシェイプまたはビューの前にくる必要があります。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def orbit(horizontalAngle: float = 1.0,pivotPoint: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rotationAngles: Tuple[float, float] = tuple(1.0, 1.0),verticalAngle: float = 1.0) -> None:
    """
    orbit コマンドはパース ウィンドウのカメラを水平または垂直に回転させます。回転軸はカメラになります。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    horizontalAngle (angle): 水平方向の回転角度です。

    -----------------------------------------

    pivotPoint ([linear, linear, linear]): ワールド空間のピボットポイントとして使用されます。

    -----------------------------------------

    rotationAngles ([angle, angle]): 水平方向および垂直方向の回転角度です。

    -----------------------------------------

    verticalAngle (angle): 垂直方向の回転角度です。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def panZoom(absolute: bool = False,downDistance: float = 1.0,leftDistance: float = 1.0,relative: bool = False,rightDistance: float = 1.0,upDistance: float = 1.0,zoomRatio: float = 1.0) -> None:
    """
    panZoom コマンドは 2D フィルムをパン/ズームします。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    absolute (boolean): このフラグは距離とzoomRatioフラグの動作を修正します。指定すると距離とzoomRatio値が直接に適用されます。

    -----------------------------------------

    downDistance (float): 下のパン距離をインチ単位で設定します

    -----------------------------------------

    leftDistance (float): 左のパン距離をインチ単位で設定します

    -----------------------------------------

    relative (boolean): このフラグは距離とzoomRatioフラグの動作を修正します。指定すると距離またはzoomRatio値がカメラの既存の値に乗算されます。既定では、relativeフラグは常にオンです。

    -----------------------------------------

    rightDistance (float): 右のパン距離をインチ単位で設定します

    -----------------------------------------

    upDistance (float): 上のパン距離をインチ単位で設定します

    -----------------------------------------

    zoomRatio (float): ズーム比率を設定します

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def perCameraVisibility(camera: str = "",exclusive: bool = False,hide: bool = False,remove: bool = False,removeAll: bool = False,removeCamera: bool = False) -> None:
    """
    perCameraVisibility コマンドでは、DAG オブジェクトとカメラ間の可視性関係の作成、照会、および除去を行います。これらの関係は、関連するカメラを使用するすべてのビューポートに適用されます(これらはレンダリングなどでは使用されません)。オブジェクトは、カメラ専用に設定したり(つまり、カメラを使用するビューポートでのみ表示され、その他のビューポートでは非表示になります)、カメラから非表示に設定する(カメラを使用するすべてのビューポートで表示されなくなります)ことができます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    camera (name): 操作するカメラを指定します。

    -----------------------------------------

    exclusive (boolean): 指定されたカメラ専用としてオブジェクトを設定します。

    -----------------------------------------

    hide (boolean): 指定されたカメラから非表示になるようにオブジェクトを設定します。

    -----------------------------------------

    remove (boolean): 専用または非表示の設定とともに使用して、オブジェクトを追加するのではなく除去します。

    -----------------------------------------

    removeAll (boolean): すべてのカメラのすべての専用/非表示オブジェクトを除去します。

    -----------------------------------------

    removeCamera (boolean): 指定されたカメラのすべての専用/非表示オブジェクトを除去します。

    -----------------------------------------

    Return Value:
    None: string[]コマンドの結果照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def roll(absolute: bool = False,degree: float = 1.0,relative: bool = False) -> None:
    """
    表示方向を中心にしてカメラを回転します。角度を正にすると、カメラは時計回りに回転し、角度を負にすると、カメラは反時計回りに回転します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    absolute (boolean): 絶対モードに設定します。

    -----------------------------------------

    degree (angle): 回転角度を設定します。

    -----------------------------------------

    relative (boolean): 相対モードに設定します。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def stereoCameraView(activeComponentsXray: bool = False,activeCustomEnvironment: str = "",activeCustomGeometry: str = "",activeCustomLighSet: str = "",activeCustomOverrideGeometry: str = "",activeCustomRenderer: str = "",activeOnly: bool = False,activeShadingGraph: str = "",activeSupported: bool = False,activeView: bool = False,addObjects: str = "",addSelected: bool = False,allObjects: bool = False,backfaceCulling: bool = False,bufferMode: str = "",bumpResolution: Tuple[int, int] = tuple(1, 1),camera: str = "",cameraName: str = "",cameraSet: str = "",cameraSetup: bool = False,cameras: bool = False,capture: str = "",captureSequenceNumber: int = 1,centerCamera: str = "",colorMap: bool = False,colorResolution: Tuple[int, int] = tuple(1, 1),control: bool = False,controlVertices: bool = False,cullingOverride: str = "",default: bool = False,defineTemplate: str = "",deformers: bool = False,dimensions: bool = False,displayAppearance: str = "",displayLights: str = "",displayMode: str = "",displayTextures: bool = False,docTag: str = "",dynamicConstraints: bool = False,dynamics: bool = False,editorChanged: str = "",exists: bool = False,filter: str = "",filteredObjectList: bool = False,fluids: bool = False,fogColor: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),fogDensity: float = 1.0,fogEnd: float = 1.0,fogMode: str = "",fogSource: str = "",fogStart: float = 1.0,fogging: bool = False,follicles: bool = False,forceMainConnection: str = "",grid: bool = False,hairSystems: bool = False,handles: bool = False,headsUpDisplay: bool = False,height: bool = False,highlightConnection: str = "",hulls: bool = False,ignorePanZoom: bool = False,ikHandles: bool = False,imagePlane: bool = False,interactive: bool = False,interactiveBackFaceCull: bool = False,interactiveDisableShadows: bool = False,isFiltered: bool = False,jointXray: bool = False,joints: bool = False,leftCamera: str = "",lights: bool = False,lineWidth: float = 1.0,locators: bool = False,lockMainConnection: bool = False,lowQualityLighting: bool = False,mainListConnection: str = "",manipulators: bool = False,maxConstantTransparency: float = 1.0,maximumNumHardwareLights: bool = False,modelPanel: str = "",motionTrails: bool = False,nCloths: bool = False,nParticles: bool = False,nRigids: bool = False,noUndo: bool = False,nurbsCurves: bool = False,nurbsSurfaces: bool = False,objectFilter: str = "",objectFilterList: str = "",objectFilterListUI: str = "",objectFilterShowInHUD: bool = False,objectFilterUI: str = "",occlusionCulling: bool = False,panel: str = "",parent: str = "",pivots: bool = False,planes: bool = False,pluginObjects: Tuple[str, bool] = tuple("", False),pluginShapes: bool = False,polymeshes: bool = False,queryPluginObjects: str = "",removeSelected: bool = False,rendererDeviceName: bool = False,rendererList: bool = False,rendererListUI: bool = False,rendererName: str = "",rendererOverrideList: bool = False,rendererOverrideListUI: bool = False,rendererOverrideName: str = "",resetCustomCamera: bool = False,rigRoot: str = "",rightCamera: str = "",sceneRenderFilter: str = "",selectionConnection: str = "",selectionHiliteDisplay: bool = False,setSelected: bool = False,shadingModel: int = 1,shadows: bool = False,smallObjectCulling: bool = False,smallObjectThreshold: float = 1.0,smoothWireframe: bool = False,sortTransparent: bool = False,stateString: bool = False,stereoDrawMode: bool = False,strokes: bool = False,subdivSurfaces: bool = False,swapEyes: bool = False,textureAnisotropic: bool = False,textureCompression: bool = False,textureDisplay: str = "",textureEnvironmentMap: bool = False,textureHilight: bool = False,textureMaxSize: int = 1,textureMemoryUsed: bool = False,textureSampling: int = 1,textures: bool = False,transpInShadows: bool = False,transparencyAlgorithm: str = "",twoSidedLighting: bool = False,unParent: bool = False,unlockMainConnection: bool = False,updateColorMode: bool = False,updateMainConnection: bool = False,useBaseRenderer: bool = False,useColorIndex: bool = False,useCustomBackground: bool = False,useDefaultMaterial: bool = False,useInteractiveMode: bool = False,useRGBImagePlane: bool = False,useReducedRenderer: bool = False,useTemplate: str = "",userNode: str = "",viewColor: Tuple[float, float, float, float] = tuple(1.0, 1.0, 1.0, 1.0),viewObjects: bool = False,viewSelected: bool = False,viewType: bool = False,width: bool = False,wireframeBackingStore: bool = False,wireframeOnShaded: bool = False,xray: bool = False) -> None:
    """
    モデル エディタの作成、編集、照会が行われます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    activeComponentsXray (boolean): アクティブコンポーネントのX線モードをオンまたはオフにします。

    -----------------------------------------

    activeCustomEnvironment (string): 環境マップとして使用するイメージファイルのパスを指定します。有効なシーンレンダーフィルタを指定した場合のみ有効です。

    -----------------------------------------

    activeCustomGeometry (string): 表示するジオメトリをオーバーライドするカスタムジオメトリの識別子を指定します。有効なシーンレンダーフィルタを指定した場合のみ有効です。

    -----------------------------------------

    activeCustomLighSet (string): シーンレンダーフィルタで使用するライトセットの識別子を指定します。有効なシーンレンダーフィルタを指定した場合のみ有効です。

    -----------------------------------------

    activeCustomOverrideGeometry (string): シーンレンダーフィルタを使用した場合のカスタムジオメトリに対するオーバーライドの識別子を指定します。

    -----------------------------------------

    activeCustomRenderer (string): 有効なシーンレンダーフィルタも指定されているときに使用するカスタムレンダラの識別子を指定します。

    -----------------------------------------

    activeOnly (boolean): シェーディング表示で、アクティブなオブジェクトのみをシェーディングした状態で表示するかどうかを設定します。

    -----------------------------------------

    activeShadingGraph (string): マテリアル表示のオーバーライドに使用するシェーディンググラフを指定します。有効なシーンレンダーフィルタを指定した場合のみ有効です。

    -----------------------------------------

    activeSupported (boolean): ビューアが、グラフィックスカード内蔵の立体サポートを利用するアクティブモードで描画できる場合はtrueを返します。これにはシャッター眼鏡のサポートとクローンモードでの立体視サポートを含みます。

    -----------------------------------------

    activeView (boolean): モデルエディタをアクティブビューに設定します。正常な場合はtrueを返します。照会すると、ビューがアクティブビューであるかどうかが返されます。

    -----------------------------------------

    addObjects (string): 選択接続に含まれるオブジェクトが、ビューで可視となるオブジェクトのリストに追加されます(viewSelectedがtrueである場合)。

    -----------------------------------------

    addSelected (boolean): 現在アクティブなオブジェクトが、ビューで可視となるオブジェクトのリストに追加されます(viewSelectedがtrueである場合)。

    -----------------------------------------

    allObjects (boolean): モデルエディタのビューですべてのオブジェクトの表示のオンとオフを切り替えます。これはNURBS、CV、ハル、グリッド、およびマニピュレータは除外します。

    -----------------------------------------

    backfaceCulling (boolean): ビュー全体のバックフェースカリングのオン/オフを切り替えます。この設定は、個々のオブジェクトのカリング設定をオーバーライドします。ビュー内に描画されるすべてのオブジェクトは、バックフェースがカリングされます。バックフェースカリングをオンにすると、法線がカメラと反対方向を向いている領域でサーフェスが表示されません。

    -----------------------------------------

    bufferMode (string): 非推奨:これはビューポート2.0ではサポートされていません。グラフィックバッファモードを設定します。指定できる値は、「single」または「double」です。

    -----------------------------------------

    bumpResolution ([uint, uint]): ハードウェアレンダラを使用する場合の、「ベイクド」バンプマップテクスチャの解像度を設定します。既定値は、それぞれ512と512です。

    -----------------------------------------

    camera (string): モデルエディタ内でカメラの名前の変更または照会が行われます。

    -----------------------------------------

    cameraName (string): パネルのカメラトランスフォームとシェイプの名前を設定します。シェイプが「選択」されている場合、トランスフォームではなくシェイプ名を返します。このフラグは照会できません。

    -----------------------------------------

    cameraSet (string): カメラセットの名前

    -----------------------------------------

    cameraSetup (boolean): 渡されたモデルエディタの名前に基づいて、カメラセットアップを含む文字列リストを返します。カメラセットアップには、互いにコネクトされている1つまたは複数のカメラが含まれます。このリスト内で、カメラのセットアップは、連続した文字列のペアとして定義されます。各ペアはアクティブカメラを特定する文字列と、指定されたアクティブカメラをセットアップするためのスクリプトを定義する文字列から構成されます。アクティブカメラと同じ数の文字列ペアが返されます。何も返されない場合、指定されたカメラをアクティブにするのにセットアップは必要ないとみなされます。

    -----------------------------------------

    cameras (boolean): モデルエディタのビューでカメラの表示のオンとオフを切り替えます。

    -----------------------------------------

    capture (string): ディスク上の指定したイメージファイルにビューポートのキャプチャを1回実行します。

    -----------------------------------------

    captureSequenceNumber (int): 0以上の値を指定すると、「capture」フラグが有効な場合、以降にリフレッシュするたびにイメージファイルがディスクに保存されます。「capture」フラグの引数に{ルート名}.{拡張子}という名前が使用されている場合、ファイル名は{ルート名}.#.{拡張子}になります。#の値はこの引数に指定した値から開始し、以降にリフレッシュするたびに増分します。「capture」フラグに0未満の値または空のファイル名を指定すると、シーケンスキャプチャを無効にできます。

    -----------------------------------------

    centerCamera (string): 照会モードのみで使用可能:このビューの現在の中央カメラを返します。

    -----------------------------------------

    colorMap (boolean): モデルパネルのカラーマップスタイルを照会します。指定できる値は、「colorIndex」および「rgb」です。

    -----------------------------------------

    colorResolution ([uint, uint]): ハードウェアレンダラを使用する場合の、「ベイクド」カラーテクスチャの解像度を設定します。既定値は、それぞれ256と256です。

    -----------------------------------------

    control (boolean): 照会モード専用です。このエディタの最上位のコントロールを返します。通常は、親を取得してポップアップメニューをアタッチするために使用します。注意:コントロールのないエディタが存在する場合があります。コントロールが存在しない場合は、この照会はNONEを返します。

    -----------------------------------------

    controlVertices (boolean): モデルエディタのビューでNURBSCVの表示のオンとオフを切り替えます。

    -----------------------------------------

    cullingOverride (string): ハードウェアレンダラを使用する場合に、オブジェクト上のカリングアトリビュートをオーバーライドするかどうかを設定します。次のオプションがあります。「none」:オブジェクトごとにカリングオブジェクトアトリビュートを使用します。「doubleSided」:すべてのオブジェクトを強制的に両面にします。「singleSided」:すべてのオブジェクトを強制的に片面にします。既定は「none」です。

    -----------------------------------------

    default (boolean): この設定の既定値が修正されます。新しく作成されるモデルエディタではこの値が継承されます。このフラグを-interactiveと一緒に使用すると、既定のインタラクティブ設定を設定できます。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    deformers (boolean): モデルエディタのビューでデフォーマオブジェクトの表示のオンとオフを切り替えます。

    -----------------------------------------

    dimensions (boolean): モデルエディタのビューで寸法オブジェクトの表示のオンとオフを切り替えます。

    -----------------------------------------

    displayAppearance (string): モデルパネルの表示の外観を設定します。有効な値は、「wireframe」、「points」、「boundingBox」、「smoothShaded」、「flatShaded」です。このフラグは、-interactiveフラグと-defaultフラグと一緒に使用できます。インタラクティブモードでは、「wireframe」、「points」、「boundingBox」のみが有効であることに注意してください。

    -----------------------------------------

    displayLights (string): シェーディングモード用にライティングを設定します。有効な値は、「selected」、「active」、「all」、「default」、「none」です。

    -----------------------------------------

    displayMode (string): このビューの表示モードを定義します。特定タイプのグラフィックスハードウェアのみで使用できるモードもあります。有効な値は、active:グラフィックスカード内蔵の立体モードがあれば、これを使用します。leftEye:左カメラのビューのみを表示します。rightEye:右カメラのビューのみを表示します。centerEye:中央カメラのビューのみを表示します。anaglyph:赤と青でフィルタした左右カメラをともに表示します。anaglyphLum:anaglyphと似ていますが、輝度は赤と青のフィルタリング前に計算されます。interlace:左右カメラをインタレースしたビューを表示します。checkerboard:interlaceと似ていますが、チェッカーボードのパターンを使用して両イメージを混合します。freeview:左右両イメージを半分のサイズで、隣り合わせに表示します。freeviewX:freeviewと似ていますが、左右カメラの位置を入れ替えます。

    -----------------------------------------

    displayTextures (boolean): シェーディングモードでのテクスチャの表示をオンまたはオフにします。

    -----------------------------------------

    docTag (string): エディタにタグをアタッチします。

    -----------------------------------------

    dynamicConstraints (boolean): モデルエディタのビューでdynamicConstraintの表示のオンとオフを切り替えます。

    -----------------------------------------

    dynamics (boolean): モデルエディタのビューでダイナミクスオブジェクトの表示のオンとオフを切り替えます。

    -----------------------------------------

    editorChanged (script): エディタオプションが変更されたときにコールされるオプションのスクリプトコールバック。これは、スクリプトパネルにmodelEditorが含まれ、そのオプションが内蔵エディタにより変更されたときに通知が必要な場合に便利です。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    filter (string): このエディタに使用する項目フィルタオブジェクトの名前を指定します。エディタの主要リストに表示される情報をフィルタします。

    -----------------------------------------

    filteredObjectList (boolean): (オブジェクトフィルタまたは選択項目の分離のいずれかを使用して)フィルタリングをオンにしたモデルエディタの場合、このフラグは、このエディタで表示されるオブジェクトの文字列リストを返します。このリストでは(カメラのフラスタムまたはフラグに基づいた)可視性は考慮されず、純粋に、ビューのレンダリング時に考慮されるオブジェクトがキャプチャされる点に注意してください。

    -----------------------------------------

    fluids (boolean): モデルエディタのビューで流体の表示のオンとオフを切り替えます。

    -----------------------------------------

    fogColor ([float, float, float, float]): ハードウェアフォグに使用するカラー。

    -----------------------------------------

    fogDensity (float): ハードウェアフォグの密度が決まります。

    -----------------------------------------

    fogEnd (float): ハードウェアフォグの終端場所。

    -----------------------------------------

    fogMode (string): フォグのドロップオフモードが決まります。指定できる値は、次のいずれかです。"linear":一次ドロップオフ"exponent":指数ドロップオフ"exponent2":二乗の指数ドロップオフ

    -----------------------------------------

    fogSource (string): 使用するフォグアルゴリズムのタイプを設定します。引数が「fragment」(既定)である場合、フォグはピクセル単位で計算されます。引数を「coordinate」にすると、ジオメトリで頂点フォグ座標を指定して、グラフィックシステムで頂点フォグのOpenGL拡張子がサポートされている場合、フォグは頂点ごとに算出されます。

    -----------------------------------------

    fogStart (float): ハードウェアフォグの開始場所。

    -----------------------------------------

    fogging (boolean): ハードウェアフォグを有効にするかどうかを設定します。

    -----------------------------------------

    follicles (boolean): モデルエディタのビューで毛根の表示のオンとオフを切り替えます。

    -----------------------------------------

    forceMainConnection (string): エディタがコンテンツのソースとして使用するselectionConnectionオブジェクトの名前を指定します。エディタはselectionConnectionオブジェクトに含まれている項目のみを表示します。これは-mainListConnectionフラグの変形で、接続がロックされている場合でも強制的に変更します。このフラグを使用して、-unlockMainConnection、-mainListConnection、-lockMainConnectionフラグを直後に連続して使用する場合に、オーバーヘッドを減します。

    -----------------------------------------

    grid (boolean): モデルエディタのビューでグリッドの表示のオンとオフを切り替えます。

    -----------------------------------------

    hairSystems (boolean): モデルエディタのビューでヘアシステムの表示のオンとオフを切り替えます。

    -----------------------------------------

    handles (boolean): モデルエディタのビューでセレクションハンドルの表示のオンとオフを切り替えます。

    -----------------------------------------

    headsUpDisplay (boolean): モデルパネルで、有効なヘッドアップディスプレイの要素をこのウィンドウに描画するか(true)どうかを設定します。現在のところ、これはヘッドアップディスプレイの要素をグローバルに有効にしておく必要があります。

    -----------------------------------------

    height (boolean): 関連付けられたビューポートの高さを返します(ピクセル単位)。

    -----------------------------------------

    highlightConnection (string): そのハイライトリストをエディタと同期化させるselectionConnectionオブジェクトの名前を指定します。すべてのエディタにハイライトリストがあるわけではありません。ハイライトリストがあるエディタの場合、これは第二の選択項目を表示したリストになります。

    -----------------------------------------

    hulls (boolean): モデルエディタのビューでNURBSハルの表示のオンとオフを切り替えます。

    -----------------------------------------

    ignorePanZoom (boolean): モデルパネルが2Dパン/ズーム値を無視し、シーンの概要を表示するかどうかを指定します。

    -----------------------------------------

    ikHandles (boolean): モデルエディタのビューでIKハンドルとエンドエフェクタの表示のオンとオフを切り替えます。

    -----------------------------------------

    imagePlane (boolean): ビューでイメージプレーンの表示のオンとオフを切り替えます。

    -----------------------------------------

    interactive (boolean): ビューのインタラクティブリフレッシュの設定を修正します。パフォーマンスを改善するため、再生中にモデルエディタの動作をこのように変更できます。

    -----------------------------------------

    interactiveBackFaceCull (boolean): インタラクティブなバックフェースカリングをオンにするかどうかを定義します。

    -----------------------------------------

    interactiveDisableShadows (boolean): インタラクティブなシャドウを無効にするかどうかを定義します。

    -----------------------------------------

    isFiltered (boolean): シーンのビューにフィルタが適用されたモデルエディタの場合はtrueを返します。これは、明示的なオブジェクトフィルタ、または、表示するオブジェクトをフィルタリングする、選択項目の分離などの表示オプションのいずれかになります。

    -----------------------------------------

    jointXray (boolean): ジョイントのX線モードをオンまたはオフにします。

    -----------------------------------------

    joints (boolean): モデルエディタのビューでジョイントの表示のオンとオフを切り替えます。

    -----------------------------------------

    leftCamera (string): 照会モードのみで使用可能:このビューの現在の左カメラを返します。

    -----------------------------------------

    lights (boolean): モデルエディタのビューでライトの表示のオンとオフを切り替えます。

    -----------------------------------------

    lineWidth (float): 表示するラインの幅を設定します。

    -----------------------------------------

    locators (boolean): モデルエディタのビューでロケータオブジェクトの表示のオンとオフを切り替えます。

    -----------------------------------------

    lockMainConnection (boolean): mainConnection内のオブジェクトの現在のリストをロックして、そのオブジェクトだけがエディタ内に表示されるようにします。これ以降、元のmainConnectionに変更を加えても無視されます。

    -----------------------------------------

    lowQualityLighting (boolean): ハードウェアレンダラを使用する場合に、「低精度ライティング」を使用するかどうかを設定します。既定値はfalseです。

    -----------------------------------------

    mainListConnection (string): エディタがコンテンツのソースとして使用するselectionConnectionオブジェクトの名前を指定します。エディタはselectionConnectionオブジェクトに含まれている項目のみを表示します。

    -----------------------------------------

    manipulators (boolean): モデルエディタのビューでマニピュレータオブジェクトの表示のオンとオフを切り替えます。

    -----------------------------------------

    maxConstantTransparency (float): コンスタントの透明度の最大値を設定します。この値を設定すると、[0.0,1.0]から[0.0,maxConstantTransparency]までの範囲でコンスタントの透明度をマップし直します。すべての透明度は新しい範囲に正比例してシフトされるため、完全に透明なオブジェクト(透明度1.0)はビューポートにmaxConstantTransparencyの透明度で表示されます。これにより、透明度の高いオブジェクトでも可視にできるようになります。このフラグは、一定の(テクスチャマッピングされていない)透明なオブジェクトにのみ影響します。

    -----------------------------------------

    maximumNumHardwareLights (boolean): ハードウェアライトの最大値が考慮されるかどうかを定義します。

    -----------------------------------------

    modelPanel (string): 作成したモデルエディタを指定したモデルパネルに埋め込むことができるようにします。APIを使用して作成されたカスタムモデルエディタと一緒に使用することを目的としています(派生したMPxModelEditorCommandでフラグを使用)が、ベースのmodelEditorコマンドでフラグを使用してパネルに既定のMayaモデルエディタを復元しても構いません。これまでパネルにあったモデルエディタは削除されていることに注意してください。

    -----------------------------------------

    motionTrails (boolean): ビューポートでモーション軌跡の表示のオンとオフを切り替えます。

    -----------------------------------------

    nCloths (boolean): モデルエディタのビューでnClothの表示のオンとオフを切り替えます。

    -----------------------------------------

    nParticles (boolean): モデルエディタのビューでnParticlesの表示のオンとオフを切り替えます。

    -----------------------------------------

    nRigids (boolean): モデルエディタのビューでnRigidの表示のオンとオフを切り替えます。

    -----------------------------------------

    noUndo (boolean): このフラグは、特定のビューポート操作(分離選択など)が元に戻す待ち行列に追加されないようにします。

    -----------------------------------------

    nurbsCurves (boolean): モデルエディタのビューでNURBSカーブの表示のオンとオフを切り替えます。

    -----------------------------------------

    nurbsSurfaces (boolean): モデルエディタのビューでNURBSサーフェスの表示のオンとオフを切り替えます。

    -----------------------------------------

    objectFilter (script): 現在のオブジェクトフィルタの名前を設定または照会します。オブジェクトフィルタは登録済みである必要があります。

    -----------------------------------------

    objectFilterList (script): 登録されたフィルタの名前のリストを返します。

    -----------------------------------------

    objectFilterListUI (script): 登録されたフィルタのUI名のリストを返します。

    -----------------------------------------

    objectFilterShowInHUD (boolean): オブジェクトフィルタがアクティブな場合に、ヘッドアップディスプレイにオブジェクトフィルタのUI名を表示するかどうかを設定します。この文字列は、カメラ名と連結します。

    -----------------------------------------

    objectFilterUI (script): 現在のオブジェクトフィルタのUI名を照会します。オブジェクトフィルタは登録済みである必要があります。

    -----------------------------------------

    occlusionCulling (boolean): ハードウェアレンダラを使用する場合に、オブジェクトが後ろに隠れるカリングテストを有効にするかどうかを設定します。既定値はfalseです。

    -----------------------------------------

    panel (string): このエディタ用のパネルを指定します。既定では、エディタがスクリプトパネルの作成コールバックで作成された場合、エディタはそのパネルに属します。エディタがパネルに属していない場合、エディタのあるウィンドウを削除するとエディタも削除されます。

    -----------------------------------------

    parent (string): このエディタの親のレイアウトを指定します。このフラグは、エディタが現在ペアレント化されていない場合のみに効果があります。

    -----------------------------------------

    pivots (boolean): モデルエディタのビューでトランスフォームピボットの表示のオンとオフを切り替えます。

    -----------------------------------------

    planes (boolean): モデルエディタのビューでスケッチプレーンの表示のオンとオフを切り替えます。

    -----------------------------------------

    pluginObjects ([string, boolean]): ビューでプラグインオブジェクトの表示のオンとオフを切り替えます。このフラグを考慮するかどうかはプラグインの実装によって異なります。

    -----------------------------------------

    pluginShapes (boolean): ビューでプラグインシェイプの表示のオンとオフを切り替えます。このフラグを考慮するかどうかはプラグインの実装によって異なります。

    -----------------------------------------

    polymeshes (boolean): モデルエディタのビューでポリゴンメッシュの表示のオンとオフを切り替えます。

    -----------------------------------------

    queryPluginObjects (string): ビューでプラグインオブジェクトの表示のオンとオフ状態を照会します。オンとオフ状態を設定する場合は、-pluginObjectsを代わりに使用します。

    -----------------------------------------

    removeSelected (boolean): 現在アクティブなオブジェクトが、ビューで可視となるオブジェクトのリストから除去されます(viewSelectedがtrueである場合)。

    -----------------------------------------

    rendererDeviceName (boolean): 3Dモデリングビューポートのビューポート2.0で使用される描画APIの名前を照会します。可能性のある戻り値は、Mayaがビューポート2.0で[OpenGL-旧式]を使用するように設定されている場合は「VirtualDeviceGL」、Mayaがビューポート2.0で[OpenGL-コアプロファイル](「厳密」と「互換性」のいずれか)を使用するように設定されている場合は「VirtualDeviceGLCore」、Mayaがビューポート2.0でDirectXを使用するように設定されている場合は「VirtualDeviceDx11」となります。3Dモデリングビューポート用のレンダラがビューポート2.0ではない場合は、空の文字列が返されます。

    -----------------------------------------

    rendererList (boolean): 3Dモデリングビューポートで使用できるレンダラの内部名のリストを照会します。サポートされている場合、既定のリストには少なくとも「vp2Renderer」が含まれています。このレンダラの詳細については、rendererNameを参照してください。このリストには、プラグインビューポートレンダラも表示されます。

    -----------------------------------------

    rendererListUI (boolean): 3Dモデリングビューポートで使用できるレンダラのUI名のリストを照会します。サポートされている場合、既定のリストには「vp2Renderer」のUI名が含まれています。このリストには、プラグインビューポートレンダラのUI名も表示されます。このリストとrendererListから返されるリストは、1:1で対応しています。

    -----------------------------------------

    rendererName (string): 3Dモデリングビューポートに使用するレンダラを設定または取得します。提供される名前はレンダラの内部名になる必要があります。「rendererList」フラグを使用して、使用可能な名前のリストを照会できます。既定のレンダラは、ビューポート2.0の「vp2Renderer」です。

    -----------------------------------------

    rendererOverrideList (boolean): 3Dビューポートレンダラで使用できるレンダラオーバーライドの内部名のリストを照会します。現在は、「Viewport2」レンダラのみがレンダラオーバーライドをサポートしています。

    -----------------------------------------

    rendererOverrideListUI (boolean): 3Dビューポートレンダラで使用できるレンダラオーバーライドのUI名のリストを照会します。現在は、「Viewport2」レンダラのみがレンダラオーバーライドをサポートしています。

    -----------------------------------------

    rendererOverrideName (string): 3Dビューポートレンダラに使用するオーバーライドを設定または取得します。提供される名前はオーバーライドの内部名になる必要があります。「rendererOverrideList」フラグを使用して、使用可能な名前のリストを照会できます。現在は、「Viewport2」レンダラのみがレンダラオーバーライドをサポートしています。空の文字列を設定すると、現在アクティブなオーバーライドの設定が解除されます。

    -----------------------------------------

    resetCustomCamera (boolean): 指定した場合、シーンレンダーフィルタに使用されるアクティブなカスタムカメラのカメラ変換をリセットします。有効なシーンレンダーフィルタを指定した場合のみ有効です。

    -----------------------------------------

    rigRoot (string): このビューにコネクトされたリグのルートを定義します。

    -----------------------------------------

    rightCamera (string): 照会モードのみで使用可能:このビューの現在の右カメラを返します。

    -----------------------------------------

    sceneRenderFilter (string): シーンレンダーフィルタの名前を指定します。

    -----------------------------------------

    selectionConnection (string): その独自のセレクションリストをエディタと同期化させるselectionConnectionオブジェクトの名前を指定します。このエディタから選択する場合、selectionConnectionオブジェクトの中から選択します。オブジェクトが変更されると、エディタが更新されて変更が反映されます。

    -----------------------------------------

    selectionHiliteDisplay (boolean): モデルパネルで、このウィンドウのオブジェクトをハイライトする選択範囲を描画するかどうかを設定します。

    -----------------------------------------

    setSelected (boolean): 現在アクティブなオブジェクトのみがビューで可視となります(viewSelectedがtrueである場合)。

    -----------------------------------------

    shadingModel (int): 使用するシェーディングモデルです。

    -----------------------------------------

    shadows (boolean): シェーディングモードで、ハードウェアシャドウの表示のオンとオフを切り替えます。

    -----------------------------------------

    smallObjectCulling (boolean): 小さなオブジェクトのカリングを有効にするかどうかを定義します。

    -----------------------------------------

    smallObjectThreshold (float): 小さなオブジェクトのカリングのしきい値です。

    -----------------------------------------

    smoothWireframe (boolean): ワイヤフレームのラインとポイントのスムージングのオンとオフを切り替えます。

    -----------------------------------------

    sortTransparent (boolean): シェーディングモードのリフレッシュ中の透明オブジェクトのソートのオンとオフを切り替えます。通常の場合、オブジェクトはカメラ空間の原点に従ってソートされますが、このフラグをオフにすると、シーングラフ内での順序(深さ優先)に従ってオブジェクトが描画されます。これはグローバルフラグで、すべてのモデルエディタに影響します。

    -----------------------------------------

    stateString (boolean): 照会モード専用のフラグです。エディタを作成して現在のエディタの状態と一致させるMELコマンドを返します。返されたコマンド文字列は、指定した名前の代わりに文字列変数$editorNameを使用します。

    -----------------------------------------

    stereoDrawMode (boolean): このフラグが使用されている場合、立体視描画モードを設定します。

    -----------------------------------------

    strokes (boolean): ビューでペイントエフェクトストロークの表示のオンとオフを切り替えます。

    -----------------------------------------

    subdivSurfaces (boolean): モデルエディタのビューでサブディビジョンサーフェスの表示のオンとオフを切り替えます。

    -----------------------------------------

    swapEyes (boolean): 左右カメラの表示を入れ替えます。左カメラは右の描画パスになり、右カメラは左の描画パスになります。このフラグは、ハードウェアが左右逆の規則を使用するような状況を想定した、上級者向けのフラグです。

    -----------------------------------------

    textureAnisotropic (boolean): 異方性マテリアルテクスチャフィルタリングを実行するかどうかが設定されます。グラフィックシステムのOpenGLで異方性テクスチャフィルタリング拡張機能がサポートされている場合に限って動作します。

    -----------------------------------------

    textureCompression (boolean): テクスチャ圧縮を使用するかどうかを定義します。

    -----------------------------------------

    textureDisplay (string): テクスチャに使用するブレンドのタイプを設定します。ブレンドは、対象フラグメントとテクスチャフラグメントの間で実行されます。一般的なソースはマテリアルカラーです。引数として、次のいずれかを指定します。modulate:対象フラグメントとテクスチャフラグメントを掛けるdecal:対象フラグメントをテクスチャフラグメントで上書きする

    -----------------------------------------

    textureEnvironmentMap (boolean): Trueの場合、テクスチャ環境マップを使用します。

    -----------------------------------------

    textureHilight (boolean): 表示がシェーディングテクスチャモードである場合に、スペキュラハイライトを表示するかどうかを設定します。

    -----------------------------------------

    textureMaxSize (int): ハードウェアテクスチャリングの最大テクスチャサイズを設定します。整数値は2の累乗である必要があります。推奨値は、128または256です。指定した値がグラフィックスハードウェア用のOpenGL最大テクスチャサイズよりも大きい場合、その値はOpenGLのサイズに固定されます。多くの巨大なテクスチャをシーン内で使用する場合、この値を下げるとパフォーマンスが向上します。ImpactではテクスチャメモリがRAMに固定されているので、大きいテクスチャを使用すると、信頼性とパフォーマンスの問題が発生することがあります。ここでも、この値を下げると問題の解決になります。ソフトウェアレンダリングでは、この値は使用されません。このフラグはMaya6.5では廃止されます。代わりに、displayPrefコマンドのmaxTextureResolution/mtr引数を使用してください。

    -----------------------------------------

    textureMemoryUsed (boolean): すべてのテクスチャマップで使用される総バイト数を返します。これは、シーン内のすべてのテクスチャオブジェクトで、幅x高さxチャネルになります。テクスチャをミップマップすると、すべてのミップマップレベルが総数に組み込まれますが、3つ以上のレベルを同時に使用することはできません。

    -----------------------------------------

    textureSampling (int): テクスチャの表示に使用するサンプリングのタイプが設定されます。引数として、次のいずれかを指定します。1:ポイントサンプリングを実行する2:バイリニア補間(既定)を実行する

    -----------------------------------------

    textures (boolean): ビューでテクスチャオブジェクトの表示のオンとオフを切り替えます。

    -----------------------------------------

    transpInShadows (boolean): ハードウェアレンダラを使用する場合に、シャドウの透明度の表示を有効にするかどうかを設定します。既定値はfalseです。

    -----------------------------------------

    transparencyAlgorithm (string): 透明度アルゴリズムを設定します。次のオプションがあります。1）frontAndBackCull:前後2つのパスのカリングテクニックです。2）perPolygonSort:後ろから前の順序のテクニックで透明なポリゴンを描画します。透明度オプション1）と2）は、ハードウェアレンダラでサポートされます。オプション1）は、インタラクティブモデリングビューポートでサポートされます。既定値は「frontAndBackCull」です。

    -----------------------------------------

    twoSidedLighting (boolean): 両面ライティングのオンとオフを切り替えます。-defaultフラグと一緒に使用できます。

    -----------------------------------------

    unParent (boolean): エディタをそのレイアウトから除去するように指定します。これは照会モードでは使用できません。

    -----------------------------------------

    unlockMainConnection (boolean): mainConnectionをロック解除して、オリジナルのmainConnection(まだ使用可能な場合)を効率的に復元し、ダイナミックな更新を行います。

    -----------------------------------------

    updateColorMode (boolean): このフラグは、どのカラーモードにするかをチェックし、それに従って切り替えるようにモデルパネルに通知します。このフラグを使用すると、カメライメージプレーンの追加か除去が実行された後でモデルパネルが更新されます。

    -----------------------------------------

    updateMainConnection (boolean): ロックされたmainConnectionをオリジナルのmainConnectionから更新させますが、ロック状態は保持されます。

    -----------------------------------------

    useBaseRenderer (boolean): ハードウェアレンダラを使用して「インタラクティブ表示モード」(-useInteractiveMode)でレンダーする場合に、「ベース」レンダラを使用するかどうかを設定します。既定値はfalseです。

    -----------------------------------------

    useColorIndex (boolean): モデルパネルで、可能な場合にカラーインデックスモードを使用するかどうかを設定されます。カラーインデックスモードでは、ポイントモード、バウンディングボックスモード、ワイヤフレーム表示モードでパフォーマンスが向上します。-defaultフラグと一緒に使用できます。

    -----------------------------------------

    useCustomBackground (boolean): trueに設定されている場合、標準のバックグラウンドを使用する代わりに、viewColorを使用してソリッドのバックグラウンドが描画されます。

    -----------------------------------------

    useDefaultMaterial (boolean): モデルパネルが、現在サーフェスに割り当てられているマテリアルを使用するのではなく、既定のマテリアルを使用してすべてのシェーディングサーフェスを描画するかどうかを設定します。

    -----------------------------------------

    useInteractiveMode (boolean): 再生中に特殊なインタラクション設定の使用のオンとオフを切り替えます。このフラグは-defaultフラグと一緒に使用できます。

    -----------------------------------------

    useRGBImagePlane (boolean): イメージプレーンがパネルのカメラにアタッチされている場合、モデルパネルをRGBモードにするかどうかを設定します。

    -----------------------------------------

    useReducedRenderer (boolean): 削減されたレンダラを使用する場合はTrueを設定します。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    userNode (string): ユーザがノード名とモデルエディタを関連付けられるようにします。値はノードの削除または名前の変更を行うイベントで自動的に更新されます。

    -----------------------------------------

    viewColor ([float, float, float, float]): 立体モデルエディタのバックグラウンドカラーを指定します。既定値は、最適の立体ビューを提供する黒です。これは、「useCustomBackground」がオン(既定)の場合にのみ適用されます。

    -----------------------------------------

    viewObjects (boolean): viewSelectedがtrueで、表示されるオブジェクトのリストがアクティブリストでない場合、ビューで可視となるオブジェクトのリストを含むobjectSetの名前が返されます(ある場合)。

    -----------------------------------------

    viewSelected (boolean): このフラグは、選択したオブジェクトの表示のオンとオフを切り替えます。このフラグをtrueに設定すると、現在アクティブなオブジェクトがキャプチャされ、表示するオブジェクトのリストとして使用されます。

    -----------------------------------------

    viewType (boolean): モデルエディタのタイプを示す文字列を返します。既定のモデルエディタの場合は、空の文字列を返します。APIを使用して作成したカスタムモデルエディタタイプの場合は、MPx3dModelView::viewType()メソッドで返される文字列と同じ文字列を返します。

    -----------------------------------------

    width (boolean): 関連付けられたビューポートの幅を返します(ピクセル単位)。

    -----------------------------------------

    wireframeBackingStore (boolean): アクティブなオブジェクトの描画の最適化にバッキングストアを使用するかどうかを設定します。このモードでは、特定のシーンのワイヤフレームモードでパフォーマンスが向上します。

    -----------------------------------------

    wireframeOnShaded (boolean): モデルパネルで、すべてのシェーディングされたオブジェクトのワイヤフレームを描画するか(true)、アクティブなオブジェクトのみのワイヤフレームを描画するか(false)を設定します。

    -----------------------------------------

    xray (boolean): X線モードをオンまたはオフにします。-defaultフラグと一緒に使用できます。

    -----------------------------------------

    Return Value:
    None: stringエディタの名前照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def stereoRigManager(addRig: Tuple[str, str, str] = tuple("", "", ""),cameraSetFunc: Tuple[str, str] = tuple("", ""),creationProcedure: Tuple[str, str] = tuple("", ""),defaultRig: str = "",delete: str = "",language: Tuple[str, str] = tuple("", ""),listRigs: bool = False,rigDefinition: str = "") -> None:
    """
    このコマンドは、立体視リグ ツールのセットを管理します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    addRig ([string, string, string]): 新しい立体視リグの定義を追加しますこのフラグは次の3つの引数を使用します:name、language、create。name:リグタイプの固有の名前です。lang:コールバックに使用する言語です。有効な値は「Python」と「MEL」です。使用可能な場合は、Pythonインタフェースを使用します。create:このタイプのリグを作成するために使用するプロシージャです。このプロシージャは引数を使用しません。また文字配列を返す必要があります。1番目のエレメントは、リグのルートDAGノードです。2番目と3番目のエレメントはそれぞれ、左側カメラと右側カメラです。

    -----------------------------------------

    cameraSetFunc ([string, string]): リグがカメラセットに追加されるときにコールする関数を指定します。この関数の言語は、ツールが元々定義する言語と同じである必要があります。

    -----------------------------------------

    creationProcedure ([string, string]): 既存のリグ定義の作成手順を変更します。このフラグは次の2つの引数を使用します:既存のリグ定義の名前と手順。

    -----------------------------------------

    defaultRig (string): 既定のリグツールを設定します。引数は、addフラグで追加したリグのうち1つの名前にする必要があります。既定が設定可能な場合はTrue、不可能な場合はFalseを返します。

    -----------------------------------------

    delete (string): 立体視リグ定義を除去します。引数は、addフラグで追加したリグのうち1つの名前にする必要があります。

    -----------------------------------------

    language ([string, string]): 既存のリグ定義の言語を変更します。有効な値は「Python」と「MEL」です。このフラグは次の2つの引数を使用します:既存のリグ定義の名前と言語キーワード。

    -----------------------------------------

    listRigs (boolean): 存在する場合、すべての定義済みリグのリストを返します。その他すべてのフラグは無視されます。

    -----------------------------------------

    rigDefinition (string): リグの定義を、addフラグと同じフォーマットで返します。lang、createcameraSetを含む文字配列です。空文字列が引数として渡された場合、デフォルトリグを使用します。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def track(down: float = 1.0,left: float = 1.0,right: float = 1.0,upDistance01: float = 1.0,upDistance02: float = 1.0) -> None:
    """
    track コマンドは、ワールド座標でカメラを水平または垂直に移動します。カメラの表示方向とアップ方向は変化しません。視線方向への移動はできません。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    down (linear): 下への移動量を単位距離で設定します。

    -----------------------------------------

    left (linear): 左への移動量を単位距離で設定します。

    -----------------------------------------

    right (linear): 右への移動量を単位距離で設定します。

    -----------------------------------------

    upDistance01 (linear): 上への移動量を単位距離で設定します。これはup/upDistance02フラグの使用と同等です。

    -----------------------------------------

    upDistance02 (linear): 上への移動量を単位距離で設定します。これはu/upDistance01フラグの使用と同等です。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def tumble(azimuthAngle: float = 1.0,elevationAngle: float = 1.0,localTumble: int = 1,pivotPoint: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rotationAngles: Tuple[float, float] = tuple(1.0, 1.0)) -> None:
    """
    tumble コマンドは、パース ビュー カメラの方位角と仰角を変更してカメラを回転させます。コマンド ライン上に方位角と仰角の両方を入力した場合、カメラはまず方位角に基づいてタンブルし、次に仰角に基づいてタンブルします。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    azimuthAngle (angle): 変更する方位角の角度です。

    -----------------------------------------

    elevationAngle (angle): 変更する仰角の角度です。

    -----------------------------------------

    localTumble (int): カメラのタンブルの中心となるポイントを記述します。0はカメラのタンブルピボット、1はカメラの注視点、2はタンブルピボットでオフセットされるカメラのローカル軸です。

    -----------------------------------------

    pivotPoint ([linear, linear, linear]): ワールド座標空間でピボットポイントとして使用される三次元ポイントです。

    -----------------------------------------

    rotationAngles ([angle, angle]): 変更する方位角と仰角の2つの角度の値です。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def viewCamera(move: str = "",sideView: bool = False,topView: bool = False) -> None:
    """
    viewCamera コマンドはカメラを配置して、別のカメラの脇や上部を直に見るために使用されます。このコマンドは、被写界深度やクリッピング プレーンを使用している際にとても便利です。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    move (name): どのカメラを動かすかを指定します。

    -----------------------------------------

    sideView (boolean): カメラをターゲットカメラの横方向を向くように動かします。

    -----------------------------------------

    topView (boolean): カメラをターゲットカメラの上方向を向くように動かします(既定)。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def viewClipPlane(autoClipPlane: bool = False,farClipPlane: float = 1.0,nearClipPlane: float = 1.0,surfacesOnly: bool = False) -> None:
    """
    viewClipPlane コマンドはカメラのクリップ プレーンを照会したり設定したりするために使用されます。カメラを指定していない場合は、アクティブなビューのカメラが使用されます。near および far クリップ プレーン フラグは auto クリップ プレーン フラグと同時に使用します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    autoClipPlane (boolean): カメラのビューフラスタム内のすべてのオブジェクトが見えるようにクリッププレーンを計算します。

    -----------------------------------------

    farClipPlane (linear): farクリッププレーンを設定、照会します。

    -----------------------------------------

    nearClipPlane (linear): nearクリッププレーンを設定、照会します。

    -----------------------------------------

    surfacesOnly (boolean): このフラグはautoClipPlaneフラグと同時に使用します。カメラのクリッピングプレーンを計算する際にサーフェスのバウンディングボックスだけを使います。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def viewFit(allObjects: bool = False,animate: bool = False,center: bool = False,fitFactor: float = 1.0,namespace: str = "",noChildren: bool = False) -> None:
    """
    viewFit コマンドは、指定したカメラを動かし、そのカメラを除くすべての選択オブジェクトがビューに入るようにします。オブジェクトが何も選択されていなければ、すべてのオブジェクトがビューにフィットされます(カメラ、ライト、スケッチ プレーンは除きます)。フィット係数は、ビューのどれくらいを覆うようにフィットするか指定できます。カメラを指定していない場合は、アクティブなビューのカメラが使用されます。カメラが動かされたあとは、注視点はオブジェクトのバウンディング ボックスの中心に設定されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    allObjects (boolean): 選択を無視してすべてのオブジェクトを対象にフィットします。

    -----------------------------------------

    animate (boolean): カメラの位置間のトランジションをアニメートするように指定します。

    -----------------------------------------

    center (boolean): 選択したオブジェクトの中心にカメラが移動し、手前に向かっては移動しないように指定します。

    -----------------------------------------

    fitFactor (float): フィットする項目がビューのどれくらいを占めるようにするかを指定します。

    -----------------------------------------

    namespace (string): 除外されるネームスペースを指定します。指定したネームスペース内のすべてのオブジェクトはフィット処理から除外されます。

    -----------------------------------------

    noChildren (boolean): フィットを決定するときに、フィットされたオブジェクトの子を無視するように指定します。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def viewHeadOn() -> None:
    """
    viewHeadOn コマンドは指定したカメラを動かし、ライブ オブジェクトの法線を「見下ろす」ようにして、そのオブジェクトにフィットさせます。ライブ オブジェクトがサーフェスであれば、任意の法線が選択されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    Return Value:
    None: なし
    """
    pass

    
def viewLookAt(position: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0)) -> None:
    """
    viewLookAt コマンドは指定したカメラを動かし、すべての選択オブジェクトの中心を向くようにします。何も選択されていなければ、カメラはグラウンド プレーンを向きます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    position ([linear, linear, linear]): カメラが向く方向のワールド座標を指定します。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def viewPlace(animate: bool = False,eyePoint: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),fieldOfView: float = 1.0,lookAt: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),ortho: bool = False,perspective: bool = False,upDirection: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),viewDirection: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0)) -> None:
    """
    このコマンドは指定したカメラを動かします。lookAt と viewDirection フラグはどちらか片方のみ使用できます。また ortho と perspective フラグもどちらか片方のみ使用できます。このコマンドで、新しいビューを指定しない状態でカメラが ortho から perspective に変わった場合などは、選択オブジェクトに関連するヒューリスティックな計算に基づきビューが決定されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    animate (boolean): trueに設定すると、現在の位置から最後の位置までのカメラトランジションがアニメートされます。

    -----------------------------------------

    eyePoint ([linear, linear, linear]): ワールド座標での視点座標を指定します。

    -----------------------------------------

    fieldOfView (angle): 視野角を設定します(パースビューカメラでは角度、正射投影カメラではワールド距離で設定します)。

    -----------------------------------------

    lookAt ([linear, linear, linear]): ワールド座標での注視点座標を指定します。

    -----------------------------------------

    ortho (boolean): カメラを正射投影カメラに設定します。

    -----------------------------------------

    perspective (boolean): カメラをパースビューカメラに設定します。

    -----------------------------------------

    upDirection ([linear, linear, linear]): Upベクトルを指定します。

    -----------------------------------------

    viewDirection ([linear, linear, linear]): 新しい視線の方向ベクトルを指定します。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def viewSet(animate: bool = False,back: bool = False,bottom: bool = False,fit: bool = False,fitFactor: float = 1.0,front: bool = False,home: bool = False,keepRenderSettings: bool = False,leftSide: bool = False,namespace: str = "",nextView: bool = False,persp: bool = False,previousView: bool = False,rightSide: bool = False,side: bool = False,top: bool = False,viewNegativeX: bool = False,viewNegativeY: bool = False,viewNegativeZ: bool = False,viewX: bool = False,viewY: bool = False,viewZ: bool = False) -> None:
    """
    このコマンドは、設定されている位置のうちの 1 つにカメラを配置します。fit フラグが persp、top、side、front と一緒に設定された場合、ビューは、選択したオブジェクトがあるときは、そのリストに基づいて「fit」されます。また、オブジェクトを選択していないときは、すべてのオブジェクトに基づいて「fit」されます。fit フラグは、軸に沿ったビューのコマンド(viewX など)と一緒に設定できないことに注意してください。カメラを指定していない場合は、アクティブなビューのカメラが使用されます。フラグが何も指定されなければ、カメラはホーム ポジションに設定されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    animate (boolean): カメラの位置間のトランジションをアニメートするように指定します。

    -----------------------------------------

    back (boolean): カメラをbackポジションに移動します。

    -----------------------------------------

    bottom (boolean): カメラをbottomポジションに移動します。

    -----------------------------------------

    fit (boolean): persp、top、side、frontにカメラを配置した後に、viewFitを実行します。

    -----------------------------------------

    fitFactor (float): フィットする項目がビューのどれくらいを占めるようにするかを指定します。

    -----------------------------------------

    front (boolean): カメラをfrontポジションに移動します。

    -----------------------------------------

    home (boolean): カメラのhomeアトリビュートコマンドを実行します。文字列を実行する前に、「%camera」があればすべてカメラの名前に置き換えられます。カメラのhomeアトリビュートコマンドを設定するには、cameraコマンドを使用します。

    -----------------------------------------

    keepRenderSettings (boolean): ビューには「renderable」フラグ値が保持されます。これはパースビューから正投影に切り替えて戻した場合に特に重要です。

    -----------------------------------------

    leftSide (boolean): カメラをleftsideポジションに移動します。

    -----------------------------------------

    namespace (string): 除外されるネームスペースを指定します。指定したネームスペース内のすべてのオブジェクトはフィット処理から除外されます。

    -----------------------------------------

    nextView (boolean): カメラを1つ後の位置に移動します。

    -----------------------------------------

    persp (boolean): カメラをperspポジションに移動します。

    -----------------------------------------

    previousView (boolean): カメラを1つ前の位置に移動します。

    -----------------------------------------

    rightSide (boolean): カメラをrightsideポジションに移動します。

    -----------------------------------------

    side (boolean): カメラを(right)sideポジションに移動します(非推奨)。

    -----------------------------------------

    top (boolean): カメラをtopポジションに移動します。

    -----------------------------------------

    viewNegativeX (boolean): 負のX軸に沿ったビューにカメラを移動します。

    -----------------------------------------

    viewNegativeY (boolean): 負のY軸に沿ったビューにカメラを移動します。

    -----------------------------------------

    viewNegativeZ (boolean): 負のZ軸に沿ったビューにカメラを移動します。

    -----------------------------------------

    viewX (boolean): X軸に沿ったビューにカメラを移動します。

    -----------------------------------------

    viewY (boolean): Y軸に沿ったビューにカメラを移動します。

    -----------------------------------------

    viewZ (boolean): Z軸に沿ったビューにカメラを移動します。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def convertIffToPsd(iffFileName: str = "",psdFileName: str = "",xResolution: int = 1,yResolution: int = 1) -> None:
    """
    IFF ファイルを指定したサイズの PSD ファイルに変換します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    iffFileName (string): 入力IFFファイル名

    -----------------------------------------

    psdFileName (string): 出力ファイル名

    -----------------------------------------

    xResolution (int): イメージのX解像度

    -----------------------------------------

    yResolution (int): イメージのY解像度

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def createLayeredPsdFile(imageFileName: Tuple[str, str, str] = tuple("", "", ""),psdFileName: str = "",xResolution: int = 1,yResolution: int = 1) -> None:
    """
    個々のレイヤにイメージ名を入力してレイヤ構造の PSD ファイルを作成します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    imageFileName ([string, string, string]): レイヤ名、ブレンドモード、イメージファイル名。ファイル内のイメージを指定されたレイヤに転送します。Mayaでサポートされているフォーマットのファイル(iff、jpg、gif、tifなど)であれば、すべてイメージファイルに指定できます。次のブレンドモードオプションがあります:Normal、Dissolve、Dark、Multiply、ColorBurn、LinearBurn、Lighten、Screen、ColorDodge、LinearDogde、Overlay、SoftLight、HardLight、Dissolve、VividLight、LinearLight、PinLight,HardMix、Difference、Exclusion、Hue、Saturation、Color、Luminosity

    -----------------------------------------

    psdFileName (string): PSDファイル名。

    -----------------------------------------

    xResolution (uint): イメージのX解像度です。

    -----------------------------------------

    yResolution (uint): イメージのY解像度です。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def createRenderLayer(empty: bool = False,g: bool = False,makeCurrent: bool = False,name: str = "",noRecurse: bool = False,number: int = 1) -> None:
    """
    新しいレンダー レイヤを作成します。レンダー レイヤには、レンダー レイヤのグローバル パラメータの基準インデックス番号より大きい、まだ割り当てられていない最初の番号が割り当てられます。通常、すべてのオブジェクトとその子孫が新規のレンダー レイヤに追加されますが、-noRecurse を指定するとオブジェクトのみが追加されます。トランスフォームとジオメトリのみが新しいレンダー レイヤに追加されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    empty (boolean): 設定すると、空のレンダーレイヤが作成されます。グローバルフラグや指定したメンバーリストは、このフラグより優先されます。

    -----------------------------------------

    g (boolean): 設定すると、シーン内にあるすべてのDAGオブジェクトを含むレイヤを作成します。以降に作成するオブジェクトも、自動的にこのレイヤのメンバーになります。グローバルフラグは、空のフラグまたは指定したメンバーリストより優先されます。

    -----------------------------------------

    makeCurrent (boolean): 設定すると、新しいレンダーレイヤが現在のレイヤになります。

    -----------------------------------------

    name (string): 作成する新しいレンダーレイヤの名前。

    -----------------------------------------

    noRecurse (boolean): 設定すると、指定したオブジェクトのみがレンダーレイヤに追加されます。設定しないと、すべての子孫も追加されます。

    -----------------------------------------

    number (int): 作成する新しいレンダーレイヤの番号。

    -----------------------------------------

    Return Value:
    None: string作成したレンダー レイヤ ノードの名前
    """
    pass

    
def editRenderLayerAdjustment(attributeLog: bool = False,layer: str = "",nodeLog: bool = False,remove: bool = False) -> None:
    """
    このコマンドを使用して、レンダー レイヤの調整を作成、編集、照会します。調整を行うことで、アクティブなレンダー レイヤに応じ、異なるアトリビュート値や接続を使用できるようになります。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    attributeLog (boolean): 指定したレイヤに対するすべての調整を、アトリビュート名順でソートして出力します。

    -----------------------------------------

    layer (name): 調整を修正するレイヤを指定します。指定しない場合、アクティブなレンダーレイヤが使用されます。

    -----------------------------------------

    nodeLog (boolean): 指定したレイヤに対するすべての調整を、ノード名順でソートして出力します。

    -----------------------------------------

    remove (boolean): 指定した調整をレンダーレイヤから除去します。現在のレイヤから調整を除去すると、指定したプラグは既定のレンダーレイヤが定義するマスター値に戻ります。

    -----------------------------------------

    Return Value:
    None: int適用された調整の数string[]照会: レイヤのプラグ調整のリスト照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def editRenderLayerGlobals(baseId: int = 1,currentRenderLayer: str = "",enableAutoAdjustments: bool = False,mergeType: int = 1,useCurrent: bool = False) -> None:
    """
    すべてのレンダー レイヤに共通するパラメータ値を編集します。baseId や mergeType などのパラメータはプリファレンスとして格納され、currentRenderLayer などのパラメータはファイルとして格納されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    baseId (int): ベースレイヤIDを設定します。これは、新しいレイヤが固有IDの検索を開始する番号です。

    -----------------------------------------

    currentRenderLayer (name): 現在のレンダーレイヤを設定することで、renderLayerMangerとすべてのDAGオブジェクトが更新され、そのレンダーレイヤのメンバーとして特定されます。このフラグを「useCurrent」と一緒に使用して、アクティブレイヤに新しいDAGオブジェクトを自動的に追加することもできます。「isCurrentRenderLayerChanging」条件を使用して、現在のレイヤが変更され、シーンへの調整が適用されるタイミングを定義することができます。

    -----------------------------------------

    enableAutoAdjustments (boolean): 特定のアトリビュート(サーフェスレンダー統計、シェーディンググループの割り当て、レンダー設定)を変更したときに、調整の自動作成を有効にするかどうかを設定します。

    -----------------------------------------

    mergeType (int): ファイルの読み込む時のマージタイプを設定します。有効な値は0(なし)、1(番号順)と2(名前順)です。

    -----------------------------------------

    useCurrent (boolean): 現在のレンダーレイヤを、すべての新規ノード目的地として使用するかどうかを設定します。

    -----------------------------------------

    Return Value:
    None: booleanコマンドの成功string照会モードでは、現在のレンダー レイヤ名int照会モードでは、マージのタイプint照会モードでは、ベース ID照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def editRenderLayerMembers(fullNames: bool = False,noRecurse: bool = False,remove: bool = False) -> None:
    """
    このコマンドを使用して、レンダー レイヤのメンバーシップを照会または編集します。メンバーになれるのは、トランスフォーム ノードおよびジオメトリ ノードに限られます。レンダー時には、レンダー レイヤのメンバーのすべての子孫もレンダー レイヤに含められます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    fullNames (boolean): (照会モード専用)設定すると、レイヤ内にあるオブジェクトのDAGのフルパスを返します。それ以外の場合は、オブジェクト名のみを返します。

    -----------------------------------------

    noRecurse (boolean): 設定すると、選択したオブジェクトのみがレンダーレイヤに追加されます。それ以外の場合は、選択したオブジェクトのすべての子孫も追加されます。このフラグを適用して、レイヤにオブジェクトを追加、またはレイヤからオブジェクトを除去することができます。

    -----------------------------------------

    remove (boolean): 指定したオブジェクトをレンダーレイヤから除去します。

    -----------------------------------------

    Return Value:
    None: intレイヤに追加されたオブジェクトの数string[]照会: レイヤ内のオブジェクトのリスト照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def frameBufferName(autoTruncate: bool = False,camera: str = "",renderLayer: str = "",renderPass: str = "") -> None:
    """
    指定した renderPass の renderLayer とカメラの組み合わせに対するフレーム バッファ名を返します。また、このコマンドではオプションで、frameBuffer 名が目的のファイル フォーマットによって指定された最大長に従うように、名前切り捨てアルゴリズムを適用できます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    autoTruncate (boolean): このフラグを使用して、該当する場合frameBuffer名が目的のファイルフォーマットによって指定された最大長に従うように、名前切り捨てアルゴリズムを適用します。

    -----------------------------------------

    camera (string): カメラを指定します。

    -----------------------------------------

    renderLayer (string): レンダラのレイヤを指定します。

    -----------------------------------------

    renderPass (string): レンダラのパスを指定します。

    -----------------------------------------

    Return Value:
    None: stringコマンドの結果
    """
    pass

    
def psdChannelOutliner(addChild: Tuple[str, str] = tuple("", ""),allItems: bool = False,annotation: str = "",backgroundColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),defineTemplate: str = "",docTag: str = "",doubleClickCommand: str = "",dragCallback: str = "",dropCallback: str = "",enable: bool = False,enableBackground: bool = False,enableKeyboardFocus: bool = False,exists: bool = False,fullPathName: bool = False,height: int = 1,highlightColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),isObscured: bool = False,manage: bool = False,noBackground: bool = False,numberOfItems: bool = False,numberOfPopupMenus: bool = False,parent: str = "",popupMenuArray: bool = False,preventOverride: bool = False,psdParent: str = "",removeAll: bool = False,removeChild: str = "",select: str = "",selectCommand: str = "",selectItem: bool = False,statusBarMessage: str = "",useTemplate: str = "",visible: bool = False,visibleChangeCommand: str = "",width: int = 1) -> None:
    """
    1 レベルまでのツリー構造を表示できる psdChannelOutliner コントロールを作成します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    addChild ([string, string]): このフラグは「-psdParent/ppa」フラグと一緒に使用する必要があります。文字列項目は「-psdParent/ppa」フラグで指定した親に子として追加されます。次の文字列によって関連付けられたイメージ名が割り当てられます。

    -----------------------------------------

    allItems (boolean): すべての項目をparent.childの形式で返します。

    -----------------------------------------

    annotation (string): コントロールに文字列値で注釈を付けます。

    -----------------------------------------

    backgroundColor ([float, float, float]): コントロールのバックグラウンドカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。backgroundColorを設定する場合、enableBackgroundをfalseに指定していない限り、バックグラウンドは自動的に有効になります。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    docTag (string): コントロールにドキュメンテーションフラグを追加します。ドキュメンテーションフラグは、ディレクトリ構造になっています。(例:-dtrender/multiLister/createNode/material)

    -----------------------------------------

    doubleClickCommand (string): 項目をダブルクリックしたときに実行するコマンドを指定します。

    -----------------------------------------

    dragCallback (script): 中マウスボタンを押すとコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalprocstring[]callbackName(string$dragControl,int$x,int$y,int$mods)procはドロップ先に転送される文字配列を返します。規則により、配列の先頭文字列はユーザ設定可能なメッセージタイプを表しています。アプリケーションで定義されたドラッグ元のコントロールは、このコールバックを無視する可能性があります。$modsで、キーモディファイアであるCTRLとSHIFTをテストできます。有効な値は、0==モディファイアなし、1==SHIFT、2==CTRL、3==CTRL+SHIFTです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defcallbackName(dragControl,x,y,modifiers):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「x」、「y」、「modifiers」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(x)d%(y)d%(modifiers)d'」)。

    -----------------------------------------

    dropCallback (script): ドラッグ＆ドロップ操作をドロップ位置で解放したときにコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalproccallbackName(string$dragControl,string$dropControl,string$msgs[],int$x,int$y,int$type)procは、ドラッグ元から転送される文字配列を受け取ります。msgs配列の先頭文字列はユーザ定義のメッセージタイプを表します。アプリケーションで定義されたドロップ先のコントロールでは、このコールバックが無視されることがあります。$typeの値は、1==移動、2==コピー、3==リンクのいずれかです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defpythonDropTest(dragControl,dropControl,messages,x,y,dragType):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「dropControl」、「messages」、「x」、「y」、「type」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(dropControl)s%(messages)r%(x)d%(y)d%(type)d'」)。

    -----------------------------------------

    enable (boolean): コントロールの有効、無効です。既定ではtrueに設定されていて、コントロールは有効になっています。falseを指定するとコントロールはグレー表示になって無効になります。

    -----------------------------------------

    enableBackground (boolean): コントロールのバックグラウンドカラーを有効にします。

    -----------------------------------------

    enableKeyboardFocus (boolean): 有効にすると、[Tab]キーを押してコントロールに移動し、キーボードまたはマウスで値を選択することができます。このフラグは通常、編集(Edit)コントロールやリスト(List)コントロールなど、既定で表示されるコントロールのフォーカスサポートをオフにする場合に使用します。無効にすると、テキストフィールド内のテキストをマウスで選択することは引き続きできますが、コピーすることはできなくなります(Linuxで[中クリックして貼り付け](MiddleClickPaste)が有効になっている場合は除きます)。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    fullPathName (boolean): すべての親を含むウィジェットのフルパス名を返します。

    -----------------------------------------

    height (int): コントロールの高さです。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    highlightColor ([float, float, float]): コントロールのハイライトカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。

    -----------------------------------------

    isObscured (boolean): コントロールが実際に表示されるかどうかを返します。コントロールは、次の場合に隠れた状態になります。非表示の場合、別のコントロールで(完全に、または部分的に)ブロックされた場合、コントロールまたは親のレイアウトを制御できない場合、あるいはコントロールのウィンドウが非表示またはアイコン化されている場合。

    -----------------------------------------

    manage (boolean): コントロールの状態を管理します。管理されていないコントロールは表示されず、画面の領域も占有しません。既定では、コントロールは管理できるように作成されます。

    -----------------------------------------

    noBackground (boolean): コントロールのバックグラウンドをクリア/リセットします。バックグラウンドは、trueを渡すと一切描画されず、falseを渡すと描画されます。このフラグの状態は、このコントロールの子に継承されます。

    -----------------------------------------

    numberOfItems (boolean): コントロールにある項目の総数です。

    -----------------------------------------

    numberOfPopupMenus (boolean): このコントロールにアタッチされるポップアップメニューの数を返します。

    -----------------------------------------

    parent (string): コントロールの親のレイアウトです。

    -----------------------------------------

    popupMenuArray (boolean): このコントロールにアタッチされる全ポップアップメニューの名前を返します。

    -----------------------------------------

    preventOverride (boolean): trueの場合、コントロールの右マウスボタンメニューを使用したコントロールアトリビュートのオーバーライドは無効になります。

    -----------------------------------------

    psdParent (string): 親として取り扱われるコントロールに項目文字列を追加します。

    -----------------------------------------

    removeAll (boolean): すべての項目をコントロールから除去します。

    -----------------------------------------

    removeChild (string): 「-psdParent/ppa」フラグで指定した親から特定の子を削除します。

    -----------------------------------------

    select (string): 名前の付いた項目を選択します。

    -----------------------------------------

    selectCommand (string): 項目を選択したときに実行するコマンドを指定します。

    -----------------------------------------

    selectItem (boolean): 選択した項目を返します。

    -----------------------------------------

    statusBarMessage (string): マウスがコントロール上にある場合にステータスバーに表示する追加の文字列です。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    visible (boolean): コントロールの可視の状態です。既定では、コントロールは表示されます。コントロールの実際の外見も、その親レイアウトの可視の状態によって異なることに注意してください。

    -----------------------------------------

    visibleChangeCommand (script): コントロールの可視の状態が変更されたときに実行されるコマンドです。

    -----------------------------------------

    width (int): コントロールの幅を指定します。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    Return Value:
    None: stringpsdChannelOutliner コントロールのフル ネーム照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def psdEditTextureFile(addChannel: str = "",addChannelColor: Tuple[str, float, float, float] = tuple("", 1.0, 1.0, 1.0),addChannelImage: Tuple[str, str] = tuple("", ""),deleteChannel: str = "",psdFileName: str = "",snapShotImage: str = "",uvSnapPostionTop: bool = False) -> None:
    """
    既存の PSD ファイルを編集します。チャネル(レイヤ セット)の追加と削除がサポートされています。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    addChannel (string): 指定した名前の空のレイヤセットを既存のPSDファイルに追加します。

    -----------------------------------------

    addChannelColor ([string, float, float, float]): (M)レイヤ名で指定したレイヤセット内に作成されるレイヤの塗り潰し色を指定します。

    -----------------------------------------

    addChannelImage ([string, string]): (M)特定のレイヤセットにレイヤとして追加する必要があるイメージのイメージファイル名を指定します。これは先頭文字列です。

    -----------------------------------------

    deleteChannel (string): (M)チャネル(レイヤセット)をPSDファイルから削除します。これは多目的フラグです。

    -----------------------------------------

    psdFileName (string): PSDファイル名。

    -----------------------------------------

    snapShotImage (string): UVスナップショット/リファレンスイメージが含まれているディスク上のイメージファイル名です。

    -----------------------------------------

    uvSnapPostionTop (boolean): PSDファイル内でのUVスナップショットイメージレイヤの位置を指定します。「true」はこのレイヤを最上位に配置し、「false」はPSDファイル内でバックグラウンドレイヤの次にある最下位にレイヤを配置します。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def psdExport(alphaChannelIdx: int = 1,bytesPerChannel: int = 1,emptyLayerSet: bool = False,format: str = "",layerName: str = "",layerSetName: str = "",outFileName: str = "",preMultiplyAlpha: bool = False,psdFileName: str = "") -> None:
    """
    Photoshop ファイルのレイヤ セットを別のフォーマットへと書き込みます。出力ファイルの深度(bpc: 1 チャネルあたりのビット数)は、入力ファイルの深度と異なる場合があります。入力が 16bpc で、出力が 8bpc の場合、データが失われます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    alphaChannelIdx (int): 出力するアルファチャネルのインデックスで、指定しない場合は既定のアルファチャネルを出力します。インデックスは0から始まります。これは、Photoshopの「AdditionalAlphaChannels」という特定のアルファチャネルを書き込む場合に便利です。

    -----------------------------------------

    bytesPerChannel (int): 出力ファイルの深度です。このキーワードは、0:入力に基づいて深度を選択1:1チャネルあたり8ビット2:1チャネルあたり16ビット既定は0です。

    -----------------------------------------

    emptyLayerSet (boolean): 指定したレイヤセットが空かどうかをチェックするためのオプションです。これは照会モードで使用し、入力ファイル名とレイヤセット名を指定する必要があります。

    -----------------------------------------

    format (string): 出力ファイルフォーマットです。このキーワードは、「iff」、「sgi」、「pic」、「tif」、「als」、「gif」、「rla」、「jpg」のいずれかです。既定はiffです。

    -----------------------------------------

    layerName (string): 出力するレイヤ名です。

    -----------------------------------------

    layerSetName (string): 出力されるレイヤセットの名前で、指定しない場合は合成イメージを出力します。照会モードでは、このフラグに値が必要になります。

    -----------------------------------------

    outFileName (string): 出力ファイルの名前(パス付き)です。

    -----------------------------------------

    preMultiplyAlpha (boolean): RGBカラーをアルファ値で乗算するオプションで、(r,g,b,a)がピクセル値である場合にこのフラグを使用すると、(r*a,g*a,b*a,a)に変更します。

    -----------------------------------------

    psdFileName (string): 入力Photoshopファイルの名前(パス付き)です。照会モードでは、このフラグに値が必要になります。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def psdTextureFile(channelRGB: Tuple[str, int, int, int, int] = tuple("", 1, 1, 1, 1),channels: Tuple[str, int, bool] = tuple("", 1, False),imageFileName: Tuple[str, str, int] = tuple("", "", 1),psdFileName: str = "",snapShotImageName: str = "",uvSnapPostionTop: bool = False,xResolution: int = 1,yResolution: int = 1) -> None:
    """
    UVSnap ショット イメージとレイヤ セット名を入力として使用して、Photoshop ファイルを作成します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    channelRGB ([string, uint, uint, uint, uint]): (M)レイヤセット名、インデックス、赤、緑、および青の値を入力として指定します。このフラグを使用して作成したレイヤは、指定したカラーで塗りつぶされます。これは多目的フラグです。このインデックスは、作成されるファイル内でのレイヤセットの配置順序を表します。

    -----------------------------------------

    channels ([string, uint, boolean]): (M)レイヤセット名とインデックスを入力として指定します。これは多目的フラグです。指定した名前を持つレイヤセットが作成されます。2番目の引数は、作成されるファイル内のレイヤセットの配置順序を表すインデックスです。3番目の引数はブーリアン値で、「true」の場合はレイヤセットの内側にレイヤが、「false」の場合は空のレイヤセットが作成されます。

    -----------------------------------------

    imageFileName ([string, string, uint]): イメージファイル名、レイヤセット名、およびインデックスです。ファイル内のイメージは、指定したレイヤセットに転送されます。このインデックスは、作成されるpsdファイル内でのレイヤセットの配置順序を表します。Mayaでサポートされているフォーマットのファイル(iff、jpg、gif、tifなど)であれば、すべてイメージファイルに指定できます。

    -----------------------------------------

    psdFileName (string): PSDファイル名。

    -----------------------------------------

    snapShotImageName (string): UVスナップショット/リファレンスイメージが含まれているディスク上のイメージファイル名です。

    -----------------------------------------

    uvSnapPostionTop (boolean): PSDファイル内でのUVスナップショットイメージレイヤの位置を指定します。「true」はこのレイヤを最上位に配置し、「false」はPSDファイル内でバックグラウンドレイヤの次にある最下位にレイヤを配置します。

    -----------------------------------------

    xResolution (uint): イメージのX解像度です。

    -----------------------------------------

    yResolution (uint): イメージのY解像度です。

    -----------------------------------------

    Return Value:
    None: なし
    """
    pass

    
def renderLayerPostProcess(keepImages: bool = False,sceneName: str = "") -> None:
    """
    レンダリング終了時に、結果のポスト プロセスを実行します。現在、個々の IFF ファイルをレイヤ化した PSD ファイルが生成されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    keepImages (boolean): オンに設定すると、PSD変換後もオリジナルのIFFイメージが維持されます。既定では除去します。

    -----------------------------------------

    sceneName (string): インタラクティブバッチレンダリングを実行するシーン名を指定します。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def renderPassRegistry(channels: int = 1,isPassSupported: bool = False,passID: str = "",passName: bool = False,renderer: str = "",supportedChannelCounts: bool = False,supportedDataTypes: bool = False,supportedPassSemantics: bool = False,supportedRenderPassNames: bool = False,supportedRenderPasses: bool = False) -> None:
    """
    レンダー パスと関連する照会情報。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    channels (int): 照会するチャネル数を指定します。

    -----------------------------------------

    isPassSupported (boolean): レンダラによってパスがサポートされているかどうかを返します。このフラグはあらかじめ-passIdで指定しておく必要があります。既定値が現在のレンダラであるレンダラは、フラグrendererによって指定されます。

    -----------------------------------------

    passID (string): 照会するレンダーパスIDを指定します。

    -----------------------------------------

    passName (boolean): passIDに使用するパス名を取得します。このフラグはあらかじめ-passIDで指定しておく必要があります。

    -----------------------------------------

    renderer (string): このコマンドを使用する際は、レンダラを指定してください。既定では、現在のレンダラが指定されます。

    -----------------------------------------

    supportedChannelCounts (boolean): レンダラ(-rendererによって指定)によってサポートされているチャネル数と、指定したパスIDをリスト表示します。このフラグはあらかじめ-passIDで指定しておく必要があります。

    -----------------------------------------

    supportedDataTypes (boolean): レンダラ(-rendererによって指定)によってサポートされているフレームバッファタイプと、指定したパスIDおよびチャネルをリスト表示します。このフラグはあらかじめ-passIDと-channelsで指定しておく必要があります。

    -----------------------------------------

    supportedPassSemantics (boolean): 指定したpassIDによってサポートされるパスセマンティクスをリスト表示します。このフラグはあらかじめ-passIdで指定しておく必要があります。

    -----------------------------------------

    supportedRenderPassNames (boolean): レンダラ(-rendererによって指定)によってサポートされているレンダーパス名リスト表示します。

    -----------------------------------------

    supportedRenderPasses (boolean): レンダラ(-rendererによって指定)によってサポートされているレンダーパスをリスト表示します。

    -----------------------------------------

    Return Value:
    None: string[]コマンドの結果
    """
    pass

    
def setRenderPassType(defaultDataType: bool = False,numChannels: int = 1,type: str = "") -> None:
    """
    このコマンドでは renderPass ノードの passID を設定し、対応するレンダー パス定義によって指定されたカスタム アトリビュートを作成します。レンダー パス ノードにすでに passID が割り当てられている場合、不要になったアトリビュートは非表示になり、必要に応じて新しいアトリビュートが表示されるかまたは作成されます。これによって、アトリビュート データを紛失することなく passID を変更したり元の値に戻したりできます。また、共通のアトリビュートを、1 つのレンダー パス タイプから次のレンダー タイプに移動することもできます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    defaultDataType (boolean): 設定すると、レンダーパスは既定のデータ型を使用します。

    -----------------------------------------

    numChannels (int): レンダーパスで使用するチャネル数を指定します。このフラグは、要求したチャネル数をサポートする実装が存在する場合のみに有効です。

    -----------------------------------------

    type (string): パスノードに割り当てるパスタイプを指定します。

    -----------------------------------------

    Return Value:
    None: booleantrue/false
    """
    pass

    
def ambientLight(ambientShade: float = 1.0,discRadius: float = 1.0,exclusive: bool = False,intensity: float = 1.0,name: str = "",position: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rgb: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rotation: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),shadowColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),shadowDither: float = 1.0,shadowSamples: int = 1,softShadow: bool = False,useRayTraceShadows: bool = False) -> None:
    """
    TlightCmd は他のライト コマンドの基本クラスです。ambientLight コマンドは、既存の ambientLight のパラメータを編集したり、新しい ambientLight を作成したりします。既定の動作は、新しい ambientLight の作成です。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    ambientShade (float): ambientShade

    -----------------------------------------

    discRadius (linear): ライトの周りの円形の半径です。

    -----------------------------------------

    exclusive (boolean): ライトが排他的に割り当てられている場合はTrue

    -----------------------------------------

    intensity (float): ライトの強度

    -----------------------------------------

    name (string): ライトの名前

    -----------------------------------------

    position ([linear, linear, linear]): ライトの位置

    -----------------------------------------

    rgb ([float, float, float]): ライトのRGBカラー

    -----------------------------------------

    rotation ([angle, angle, angle]): 方向指定のためのライトの回転(該当する場合)

    -----------------------------------------

    shadowColor ([float, float, float]): ライトのシャドウの色

    -----------------------------------------

    shadowDither (float): シャドウをディザリングします。

    -----------------------------------------

    shadowSamples (int): シャドウサンプルの数です。

    -----------------------------------------

    softShadow (boolean): ソフトシャドウです。

    -----------------------------------------

    useRayTraceShadows (boolean): レイトレースのシャドウを使用する場合はTrue

    -----------------------------------------

    Return Value:
    None: double[]rgb または shadowColor フラグ(double)を照会する場合、intensity フラグ(boolean)を照会する場合、useRayTraceShadows または exclusive フラグ(linear[])を照会する場合、position フラグ(angle[])を照会する場合、rotation フラグ(string)を照会する場合、name フラグを照会する場合stringライト シェイプの名前照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def defaultLightListCheckBox(annotation: str = "",backgroundColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),defineTemplate: str = "",docTag: str = "",dragCallback: str = "",dropCallback: str = "",enable: bool = False,enableBackground: bool = False,enableKeyboardFocus: bool = False,exists: bool = False,fullPathName: bool = False,height: int = 1,highlightColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),isObscured: bool = False,label: str = "",manage: bool = False,noBackground: bool = False,numberOfPopupMenus: bool = False,parent: str = "",popupMenuArray: bool = False,preventOverride: bool = False,shadingGroup: str = "",statusBarMessage: str = "",useTemplate: str = "",visible: bool = False,visibleChangeCommand: str = "",width: int = 1) -> None:
    """
    このコマンドは、shadingGroup を defaultLightList との接続/切り離しを制御するチェックボックスを作成します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    annotation (string): コントロールに文字列値で注釈を付けます。

    -----------------------------------------

    backgroundColor ([float, float, float]): コントロールのバックグラウンドカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。backgroundColorを設定する場合、enableBackgroundをfalseに指定していない限り、バックグラウンドは自動的に有効になります。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    docTag (string): コントロールにドキュメンテーションフラグを追加します。ドキュメンテーションフラグは、ディレクトリ構造になっています。(例:-dtrender/multiLister/createNode/material)

    -----------------------------------------

    dragCallback (script): 中マウスボタンを押すとコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalprocstring[]callbackName(string$dragControl,int$x,int$y,int$mods)procはドロップ先に転送される文字配列を返します。規則により、配列の先頭文字列はユーザ設定可能なメッセージタイプを表しています。アプリケーションで定義されたドラッグ元のコントロールは、このコールバックを無視する可能性があります。$modsで、キーモディファイアであるCTRLとSHIFTをテストできます。有効な値は、0==モディファイアなし、1==SHIFT、2==CTRL、3==CTRL+SHIFTです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defcallbackName(dragControl,x,y,modifiers):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「x」、「y」、「modifiers」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(x)d%(y)d%(modifiers)d'」)。

    -----------------------------------------

    dropCallback (script): ドラッグ＆ドロップ操作をドロップ位置で解放したときにコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalproccallbackName(string$dragControl,string$dropControl,string$msgs[],int$x,int$y,int$type)procは、ドラッグ元から転送される文字配列を受け取ります。msgs配列の先頭文字列はユーザ定義のメッセージタイプを表します。アプリケーションで定義されたドロップ先のコントロールでは、このコールバックが無視されることがあります。$typeの値は、1==移動、2==コピー、3==リンクのいずれかです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defpythonDropTest(dragControl,dropControl,messages,x,y,dragType):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「dropControl」、「messages」、「x」、「y」、「type」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(dropControl)s%(messages)r%(x)d%(y)d%(type)d'」)。

    -----------------------------------------

    enable (boolean): コントロールの有効、無効です。既定ではtrueに設定されていて、コントロールは有効になっています。falseを指定するとコントロールはグレー表示になって無効になります。

    -----------------------------------------

    enableBackground (boolean): コントロールのバックグラウンドカラーを有効にします。

    -----------------------------------------

    enableKeyboardFocus (boolean): 有効にすると、[Tab]キーを押してコントロールに移動し、キーボードまたはマウスで値を選択することができます。このフラグは通常、編集(Edit)コントロールやリスト(List)コントロールなど、既定で表示されるコントロールのフォーカスサポートをオフにする場合に使用します。無効にすると、テキストフィールド内のテキストをマウスで選択することは引き続きできますが、コピーすることはできなくなります(Linuxで[中クリックして貼り付け](MiddleClickPaste)が有効になっている場合は除きます)。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    fullPathName (boolean): すべての親を含むウィジェットのフルパス名を返します。

    -----------------------------------------

    height (int): コントロールの高さです。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    highlightColor ([float, float, float]): コントロールのハイライトカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。

    -----------------------------------------

    isObscured (boolean): コントロールが実際に表示されるかどうかを返します。コントロールは、次の場合に隠れた状態になります。非表示の場合、別のコントロールで(完全に、または部分的に)ブロックされた場合、コントロールまたは親のレイアウトを制御できない場合、あるいはコントロールのウィンドウが非表示またはアイコン化されている場合。

    -----------------------------------------

    label (string): チェックボックスラベルの値です。

    -----------------------------------------

    manage (boolean): コントロールの状態を管理します。管理されていないコントロールは表示されず、画面の領域も占有しません。既定では、コントロールは管理できるように作成されます。

    -----------------------------------------

    noBackground (boolean): コントロールのバックグラウンドをクリア/リセットします。バックグラウンドは、trueを渡すと一切描画されず、falseを渡すと描画されます。このフラグの状態は、このコントロールの子に継承されます。

    -----------------------------------------

    numberOfPopupMenus (boolean): このコントロールにアタッチされるポップアップメニューの数を返します。

    -----------------------------------------

    parent (string): コントロールの親のレイアウトです。

    -----------------------------------------

    popupMenuArray (boolean): このコントロールにアタッチされる全ポップアップメニューの名前を返します。

    -----------------------------------------

    preventOverride (boolean): trueの場合、コントロールの右マウスボタンメニューを使用したコントロールアトリビュートのオーバーライドは無効になります。

    -----------------------------------------

    shadingGroup (name): defaultLightListと接続/切り離しをするシェーディンググループです。

    -----------------------------------------

    statusBarMessage (string): マウスがコントロール上にある場合にステータスバーに表示する追加の文字列です。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    visible (boolean): コントロールの可視の状態です。既定では、コントロールは表示されます。コントロールの実際の外見も、その親レイアウトの可視の状態によって異なることに注意してください。

    -----------------------------------------

    visibleChangeCommand (script): コントロールの可視の状態が変更されたときに実行されるコマンドです。

    -----------------------------------------

    width (int): コントロールの幅を指定します。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    Return Value:
    None: stringコントロールのフル ネーム照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def directionalLight(decayRate: int = 1,discRadius: float = 1.0,exclusive: bool = False,intensity: float = 1.0,name: str = "",position: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rgb: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rotation: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),shadowColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),shadowDither: float = 1.0,shadowSamples: int = 1,softShadow: bool = False,useRayTraceShadows: bool = False) -> None:
    """
    TlightCmd は他のライト コマンドの基本クラスです。TnonAmbientLightCmd クラスはコマンドのように見えますが、コマンドではありません。延長/非延長ライトの基本クラスです。TnonExtendedLightCmd は基本クラスであり、実際のコマンドではありません。 このクラスはいくつかのライト(TpointLight、TdirectionalLight、TspotLight など)で継承されます。既存のディレクショナル ライトのパラメータを編集するか、新しいディレクショナル ライトを作成するために使用します。既定では、新しいディレクショナル ライトが作成されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    decayRate (int): ライトの減衰度です(0-減衰なし、1-ゆっくり減衰、2-普通の減衰、3-速い減衰)。

    -----------------------------------------

    discRadius (linear): シャドウディスクの半径です。

    -----------------------------------------

    exclusive (boolean): ライトが排他的に割り当てられている場合はTrue

    -----------------------------------------

    intensity (float): ライトの強度

    -----------------------------------------

    name (string): ライトの名前

    -----------------------------------------

    position ([linear, linear, linear]): ライトの位置

    -----------------------------------------

    rgb ([float, float, float]): ライトのRGBカラー

    -----------------------------------------

    rotation ([angle, angle, angle]): 方向指定のためのライトの回転(該当する場合)

    -----------------------------------------

    shadowColor ([float, float, float]): ライトのシャドウの色

    -----------------------------------------

    shadowDither (float): シャドウディザリング値。

    -----------------------------------------

    shadowSamples (int): 使用するシャドウサンプルの数

    -----------------------------------------

    softShadow (boolean): ソフトシャドウを有効にする場合はTrue

    -----------------------------------------

    useRayTraceShadows (boolean): レイトレースのシャドウを使用する場合はTrue

    -----------------------------------------

    Return Value:
    None: double[]rgb または shadowColor フラグ(double)を照会する場合、intensity フラグ(boolean)を照会する場合、useRayTraceShadows または exclusive フラグ(linear[])を照会する場合、position フラグ(angle[])を照会する場合、rotation フラグ(string)を照会する場合、name フラグを照会する場合intdecayRate フラグを照会する場合はライトの減衰度intShadowSamples フラグ(boolean)を照会する場合はシャドウ サンプルの数、ソフト シャドウが有効な場合に softShadow フラグ(float)を照会する場合は True、shadowDither フラグ(float)を照会する場合はシャドウ ディザリング値、discRadius フラグを照会する場合はディスクの半径値stringライト シェイプの名前照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def exclusiveLightCheckBox(annotation: str = "",backgroundColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),defineTemplate: str = "",docTag: str = "",dragCallback: str = "",dropCallback: str = "",enable: bool = False,enableBackground: bool = False,enableKeyboardFocus: bool = False,exists: bool = False,fullPathName: bool = False,height: int = 1,highlightColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),isObscured: bool = False,label: str = "",light: str = "",manage: bool = False,noBackground: bool = False,numberOfPopupMenus: bool = False,parent: str = "",popupMenuArray: bool = False,preventOverride: bool = False,statusBarMessage: str = "",useTemplate: str = "",visible: bool = False,visibleChangeCommand: str = "",width: int = 1) -> None:
    """
    このコマンドは、ライトの排他、非排他の状態を制御する checkBox を作成します。排他ライトは、既定のライト リストにないライトで、既定のすべてのオブジェクトを照らすわけではありません。ただし、排他ライトをオブジェクトに関連付けることはできます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    annotation (string): コントロールに文字列値で注釈を付けます。

    -----------------------------------------

    backgroundColor ([float, float, float]): コントロールのバックグラウンドカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。backgroundColorを設定する場合、enableBackgroundをfalseに指定していない限り、バックグラウンドは自動的に有効になります。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    docTag (string): コントロールにドキュメンテーションフラグを追加します。ドキュメンテーションフラグは、ディレクトリ構造になっています。(例:-dtrender/multiLister/createNode/material)

    -----------------------------------------

    dragCallback (script): 中マウスボタンを押すとコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalprocstring[]callbackName(string$dragControl,int$x,int$y,int$mods)procはドロップ先に転送される文字配列を返します。規則により、配列の先頭文字列はユーザ設定可能なメッセージタイプを表しています。アプリケーションで定義されたドラッグ元のコントロールは、このコールバックを無視する可能性があります。$modsで、キーモディファイアであるCTRLとSHIFTをテストできます。有効な値は、0==モディファイアなし、1==SHIFT、2==CTRL、3==CTRL+SHIFTです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defcallbackName(dragControl,x,y,modifiers):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「x」、「y」、「modifiers」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(x)d%(y)d%(modifiers)d'」)。

    -----------------------------------------

    dropCallback (script): ドラッグ＆ドロップ操作をドロップ位置で解放したときにコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalproccallbackName(string$dragControl,string$dropControl,string$msgs[],int$x,int$y,int$type)procは、ドラッグ元から転送される文字配列を受け取ります。msgs配列の先頭文字列はユーザ定義のメッセージタイプを表します。アプリケーションで定義されたドロップ先のコントロールでは、このコールバックが無視されることがあります。$typeの値は、1==移動、2==コピー、3==リンクのいずれかです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defpythonDropTest(dragControl,dropControl,messages,x,y,dragType):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「dropControl」、「messages」、「x」、「y」、「type」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(dropControl)s%(messages)r%(x)d%(y)d%(type)d'」)。

    -----------------------------------------

    enable (boolean): コントロールの有効、無効です。既定ではtrueに設定されていて、コントロールは有効になっています。falseを指定するとコントロールはグレー表示になって無効になります。

    -----------------------------------------

    enableBackground (boolean): コントロールのバックグラウンドカラーを有効にします。

    -----------------------------------------

    enableKeyboardFocus (boolean): 有効にすると、[Tab]キーを押してコントロールに移動し、キーボードまたはマウスで値を選択することができます。このフラグは通常、編集(Edit)コントロールやリスト(List)コントロールなど、既定で表示されるコントロールのフォーカスサポートをオフにする場合に使用します。無効にすると、テキストフィールド内のテキストをマウスで選択することは引き続きできますが、コピーすることはできなくなります(Linuxで[中クリックして貼り付け](MiddleClickPaste)が有効になっている場合は除きます)。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    fullPathName (boolean): すべての親を含むウィジェットのフルパス名を返します。

    -----------------------------------------

    height (int): コントロールの高さです。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    highlightColor ([float, float, float]): コントロールのハイライトカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。

    -----------------------------------------

    isObscured (boolean): コントロールが実際に表示されるかどうかを返します。コントロールは、次の場合に隠れた状態になります。非表示の場合、別のコントロールで(完全に、または部分的に)ブロックされた場合、コントロールまたは親のレイアウトを制御できない場合、あるいはコントロールのウィンドウが非表示またはアイコン化されている場合。

    -----------------------------------------

    label (string): チェックボックスラベルの値です。

    -----------------------------------------

    light (name): 排他または非排他にするライトです。

    -----------------------------------------

    manage (boolean): コントロールの状態を管理します。管理されていないコントロールは表示されず、画面の領域も占有しません。既定では、コントロールは管理できるように作成されます。

    -----------------------------------------

    noBackground (boolean): コントロールのバックグラウンドをクリア/リセットします。バックグラウンドは、trueを渡すと一切描画されず、falseを渡すと描画されます。このフラグの状態は、このコントロールの子に継承されます。

    -----------------------------------------

    numberOfPopupMenus (boolean): このコントロールにアタッチされるポップアップメニューの数を返します。

    -----------------------------------------

    parent (string): コントロールの親のレイアウトです。

    -----------------------------------------

    popupMenuArray (boolean): このコントロールにアタッチされる全ポップアップメニューの名前を返します。

    -----------------------------------------

    preventOverride (boolean): trueの場合、コントロールの右マウスボタンメニューを使用したコントロールアトリビュートのオーバーライドは無効になります。

    -----------------------------------------

    statusBarMessage (string): マウスがコントロール上にある場合にステータスバーに表示する追加の文字列です。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    visible (boolean): コントロールの可視の状態です。既定では、コントロールは表示されます。コントロールの実際の外見も、その親レイアウトの可視の状態によって異なることに注意してください。

    -----------------------------------------

    visibleChangeCommand (script): コントロールの可視の状態が変更されたときに実行されるコマンドです。

    -----------------------------------------

    width (int): コントロールの幅を指定します。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    Return Value:
    None: stringコントロールのフル ネーム照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def lightlink(b: bool = False,hierarchy: bool = False,light: str = "",make: bool = False,object: str = "",sets: bool = False,shadow: bool = False,shapes: bool = False,transforms: bool = False,useActiveLights: bool = False,useActiveObjects: bool = False) -> None:
    """
    ライトまたはライト セットとオブジェクトまたはオブジェクト セットの間で、ライトのリンクリレーションの作成、破壊、照会を実行するために使用します。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    b (boolean): コマンドでこのフラグを指定すると、ライトとレンダリング可能オブジェクトの間でリンクを破壊するためにコマンドが呼び出されます。

    -----------------------------------------

    hierarchy (boolean): 照会する場合は、照会するライトやオブジェクトにリンクされたシェイプの上のトランスフォームの階層を結果に含めるかどうかを指定します。階層の一部とみなされるトランスフォームには、シェイプのすぐ上のトランスフォームが含まれません。既定はtrueです。

    -----------------------------------------

    light (name): lightフラグの引数は、アクションの実行でコマンドが使用するノードを、そのノードがライトであるかのように指定します。これは多重使用フラグです。つまりlightlinkコマンドの1回の呼出しで複数のライトノードを指定できます。

    -----------------------------------------

    make (boolean): コマンドでこのフラグを指定すると、ライトとレンダリング可能オブジェクトの間にリンクを作成するためにコマンドが呼び出されます。

    -----------------------------------------

    object (name): objectフラグの引数は、アクションの実行でコマンドが使用するノードを、そのノードがオブジェクトであるかのように指定します。これは多重使用フラグです。つまりlightlinkコマンドの1回の呼出しで複数のオブジェクトノードを指定できます。

    -----------------------------------------

    sets (boolean): 照会する場合は、照会するライトやオブジェクトにリンクされたセットを結果に含めるかどうかを指定します。既定はtrueです。

    -----------------------------------------

    shadow (boolean): シャドウがリンクされるかどうかを指定します。

    -----------------------------------------

    shapes (boolean): 照会する場合は、照会するライトやオブジェクトにリンクされたシェイプを結果に含めるかどうかを指定します。既定はtrueです。

    -----------------------------------------

    transforms (boolean): 照会する場合は、照会するライトやオブジェクトにリンクされたシェイプの上のトランスフォームを結果に含めるかどうかを指定します。既定はtrueです。

    -----------------------------------------

    useActiveLights (boolean): アクティブなライトが使用されるかどうかを指定します。

    -----------------------------------------

    useActiveObjects (boolean): アクティブなオブジェクトが使用されるかどうかを指定します。

    -----------------------------------------

    Return Value:
    None: string単一要素のコマンドの結果string[]複数要素のコマンドの結果照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def lightList(add: str = "",remove: str = "") -> None:
    """
    オブジェクトと現在のライトのリレーションの追加と除去が行われます。近日中に connect-attribute コマンドで置き換えられる予定です。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    add (name): ライトリストにオブジェクトが追加されます。

    -----------------------------------------

    remove (name): ライトリストからオブジェクトが除去されます。

    -----------------------------------------

    Return Value:
    None: なし照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def pointLight(decayRate: int = 1,discRadius: float = 1.0,exclusive: bool = False,intensity: float = 1.0,name: str = "",position: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rgb: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rotation: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),shadowColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),shadowDither: float = 1.0,shadowSamples: int = 1,softShadow: bool = False,useRayTraceShadows: bool = False) -> None:
    """
    既存ポイントライトのパラメータの編集、または新しいポイントライトの作成に使用します。既定では、新しいポイントライトが作成されます。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    decayRate (int): ライトの減衰度です(0-減衰なし、1-ゆっくり減衰、2-普通の減衰、3-速い減衰)。

    -----------------------------------------

    discRadius (linear): ライトの周りの円形の半径です。

    -----------------------------------------

    exclusive (boolean): このフラグは現在サポートしていません。

    -----------------------------------------

    intensity (float): ライトの輝度です(パーセンテージ表示)。

    -----------------------------------------

    name (string): ライトの名前を指定します。

    -----------------------------------------

    position ([linear, linear, linear]): このフラグは現在サポートしていません。

    -----------------------------------------

    rgb ([float, float, float]): ライトのカラーです(0-1)。

    -----------------------------------------

    rotation ([angle, angle, angle]): このフラグは現在サポートしていません。

    -----------------------------------------

    shadowColor ([float, float, float]): シャドウカラーです。

    -----------------------------------------

    shadowDither (float): シャドウをディザリングします。

    -----------------------------------------

    shadowSamples (int): シャドウサンプルの数です。

    -----------------------------------------

    softShadow (boolean): ソフトシャドウです。

    -----------------------------------------

    useRayTraceShadows (boolean): レイトレースシャドウです。

    -----------------------------------------

    Return Value:
    None: stringライト シェイプの名前照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def spotLight(barnDoors: bool = False,bottomBarnDoorAngle: float = 1.0,coneAngle: float = 1.0,decayRate: int = 1,discRadius: float = 1.0,dropOff: float = 1.0,exclusive: bool = False,intensity: float = 1.0,leftBarnDoorAngle: float = 1.0,name: str = "",penumbra: float = 1.0,position: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rgb: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),rightBarnDoorAngle: float = 1.0,rotation: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),shadowColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),shadowDither: float = 1.0,shadowSamples: int = 1,softShadow: bool = False,topBarnDoorAngle: float = 1.0,useRayTraceShadows: bool = False) -> None:
    """
    TlightCmd は他のライト コマンドの基本クラスです。TnonAmbientLightCmd クラスはコマンドのように見えますが、コマンドではありません。延長/非延長ライトの基本クラスです。TnonExtendedLightCmd は基本クラスであり、実際のコマンドではありません。 このクラスはいくつかのライト(TpointLight、TdirectionalLight、TspotLight など)で継承されます。spotLight コマンドは、既存のスポット ライトのパラメータを編集したり、新しいスポット ライトを作成したりするために使用します。既定動作は、新しいスポットライトの作成です。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    barnDoors (boolean): バーンドアは有効になっていますか?

    -----------------------------------------

    bottomBarnDoorAngle (angle): バーンドアの下部の角度です。

    -----------------------------------------

    coneAngle (angle): スポットライトの角度です。

    -----------------------------------------

    decayRate (int): ライトの減衰度です(0-減衰なし、1-ゆっくり減衰、2-普通の減衰、3-速い減衰)。

    -----------------------------------------

    discRadius (linear): シャドウディスクの半径です。

    -----------------------------------------

    dropOff (float): スポットライトのドロップオフです。

    -----------------------------------------

    exclusive (boolean): ライトが排他的に割り当てられている場合はTrue

    -----------------------------------------

    intensity (float): ライトの強度

    -----------------------------------------

    leftBarnDoorAngle (angle): バーンドアの左側の角度です。

    -----------------------------------------

    name (string): ライトの名前

    -----------------------------------------

    penumbra (angle): 周縁部の領域を指定します。

    -----------------------------------------

    position ([linear, linear, linear]): ライトの位置

    -----------------------------------------

    rgb ([float, float, float]): ライトのRGBカラー

    -----------------------------------------

    rightBarnDoorAngle (angle): バーンドアの右側の角度です。

    -----------------------------------------

    rotation ([angle, angle, angle]): 方向指定のためのライトの回転(該当する場合)

    -----------------------------------------

    shadowColor ([float, float, float]): ライトのシャドウの色

    -----------------------------------------

    shadowDither (float): シャドウディザリング値。

    -----------------------------------------

    shadowSamples (int): 使用するシャドウサンプルの数

    -----------------------------------------

    softShadow (boolean): ソフトシャドウを有効にする場合はTrue

    -----------------------------------------

    topBarnDoorAngle (angle): バーンドアの上部の角度です。

    -----------------------------------------

    useRayTraceShadows (boolean): レイトレースのシャドウを使用する場合はTrue

    -----------------------------------------

    Return Value:
    None: stringライト シェイプ名(boolean)、バーン ドアが有効状態(角度)、左バーン ドア角度(角度)、右左バーン ドア角度(角度)、上バーン ドア角度(角度)、下バーン ドア角度(角度)、円錐角度(角度)、周縁部の角度(float)、Dropoff 値double[]rgb または shadowColor フラグ(double)を照会する場合、intensity フラグ(boolean)を照会する場合、useRayTraceShadows または exclusive フラグ(linear[])を照会する場合、position フラグ(angle[])を照会する場合、rotation フラグ(string)を照会する場合、name フラグを照会する場合intdecayRate フラグを照会する場合はライトの減衰度intShadowSamples フラグ(boolean)を照会する場合はシャドウ サンプルの数、ソフト シャドウが有効な場合に softShadow フラグ(float)を照会する場合は True、shadowDither フラグ(float)を照会する場合はシャドウ ディザリング値、discRadius フラグを照会する場合はディスクの半径値照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    
def spotLightPreviewPort(annotation: str = "",backgroundColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),defineTemplate: str = "",docTag: str = "",dragCallback: str = "",dropCallback: str = "",enable: bool = False,enableBackground: bool = False,enableKeyboardFocus: bool = False,exists: bool = False,fullPathName: bool = False,height: int = 1,highlightColor: Tuple[float, float, float] = tuple(1.0, 1.0, 1.0),isObscured: bool = False,manage: bool = False,noBackground: bool = False,numberOfPopupMenus: bool = False,parent: str = "",popupMenuArray: bool = False,preventOverride: bool = False,spotLight: str = "",statusBarMessage: str = "",useTemplate: str = "",visible: bool = False,visibleChangeCommand: str = "",width: int = 1,widthHeight: Tuple[int, int] = tuple(1, 1)) -> None:
    """
    このコマンドは、スポット ライトの照度を表すイメージを表示する 3dPort を作成します。3dPort は、ライトによって照らされているプレーンのピクチャです。



    -----------------------------------------

    Flags:

    -----------------------------------------
    
    annotation (string): コントロールに文字列値で注釈を付けます。

    -----------------------------------------

    backgroundColor ([float, float, float]): コントロールのバックグラウンドカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。backgroundColorを設定する場合、enableBackgroundをfalseに指定していない限り、バックグラウンドは自動的に有効になります。

    -----------------------------------------

    defineTemplate (string): 他の任意のフラグと引数を解析し、かつ引数で指定したコマンドテンプレートに追加するモードに、コマンドのモードを変更します。templateNameが現在のテンプレートとして設定されていれば、その後コマンドが実行されるたびに、この引数が既定の引数として使用されます。

    -----------------------------------------

    docTag (string): コントロールにドキュメンテーションフラグを追加します。ドキュメンテーションフラグは、ディレクトリ構造になっています。(例:-dtrender/multiLister/createNode/material)

    -----------------------------------------

    dragCallback (script): 中マウスボタンを押すとコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalprocstring[]callbackName(string$dragControl,int$x,int$y,int$mods)procはドロップ先に転送される文字配列を返します。規則により、配列の先頭文字列はユーザ設定可能なメッセージタイプを表しています。アプリケーションで定義されたドラッグ元のコントロールは、このコールバックを無視する可能性があります。$modsで、キーモディファイアであるCTRLとSHIFTをテストできます。有効な値は、0==モディファイアなし、1==SHIFT、2==CTRL、3==CTRL+SHIFTです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defcallbackName(dragControl,x,y,modifiers):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「x」、「y」、「modifiers」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(x)d%(y)d%(modifiers)d'」)。

    -----------------------------------------

    dropCallback (script): ドラッグ＆ドロップ操作をドロップ位置で解放したときにコールされるコールバックを追加します。MELバージョンのコールバックの書式は次のとおりです。globalproccallbackName(string$dragControl,string$dropControl,string$msgs[],int$x,int$y,int$type)procは、ドラッグ元から転送される文字配列を受け取ります。msgs配列の先頭文字列はユーザ定義のメッセージタイプを表します。アプリケーションで定義されたドロップ先のコントロールでは、このコールバックが無視されることがあります。$typeの値は、1==移動、2==コピー、3==リンクのいずれかです。Pythonでも同様ですが、コールバックの指定方法が2つあります。お勧めの方法は、引数としてPython関数オブジェクトを渡すことです。この場合、Pythonコールバックの書式は次のようになります。defpythonDropTest(dragControl,dropControl,messages,x,y,dragType):この引数の値は、上記のMELバージョンの引数と同じです。Pythonでコールバックを指定するもう1つの方法では、実行する文字列を指定します。この場合、Pythonの標準的なフォーマット演算子を介して文字列に値が代入されます。このフォーマットの値は、キー「dragControl」、「dropControl」、「messages」、「x」、「y」、「type」と共に辞書で渡されます。dragControlの値は文字列で、その他の値は整数です(コールバック文字列の例:「print'%(dragControl)s%(dropControl)s%(messages)r%(x)d%(y)d%(type)d'」)。

    -----------------------------------------

    enable (boolean): コントロールの有効、無効です。既定ではtrueに設定されていて、コントロールは有効になっています。falseを指定するとコントロールはグレー表示になって無効になります。

    -----------------------------------------

    enableBackground (boolean): コントロールのバックグラウンドカラーを有効にします。

    -----------------------------------------

    enableKeyboardFocus (boolean): 有効にすると、[Tab]キーを押してコントロールに移動し、キーボードまたはマウスで値を選択することができます。このフラグは通常、編集(Edit)コントロールやリスト(List)コントロールなど、既定で表示されるコントロールのフォーカスサポートをオフにする場合に使用します。無効にすると、テキストフィールド内のテキストをマウスで選択することは引き続きできますが、コピーすることはできなくなります(Linuxで[中クリックして貼り付け](MiddleClickPaste)が有効になっている場合は除きます)。

    -----------------------------------------

    exists (boolean): 指定したオブジェクトが存在するかどうかを返します。他のフラグは無視されます。

    -----------------------------------------

    fullPathName (boolean): すべての親を含むウィジェットのフルパス名を返します。

    -----------------------------------------

    height (int): コントロールの高さです。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    highlightColor ([float, float, float]): コントロールのハイライトカラーです。引数は、赤、緑、青のカラー成分に対応しています。それぞれの成分の値は、0.0～1.0です。

    -----------------------------------------

    isObscured (boolean): コントロールが実際に表示されるかどうかを返します。コントロールは、次の場合に隠れた状態になります。非表示の場合、別のコントロールで(完全に、または部分的に)ブロックされた場合、コントロールまたは親のレイアウトを制御できない場合、あるいはコントロールのウィンドウが非表示またはアイコン化されている場合。

    -----------------------------------------

    manage (boolean): コントロールの状態を管理します。管理されていないコントロールは表示されず、画面の領域も占有しません。既定では、コントロールは管理できるように作成されます。

    -----------------------------------------

    noBackground (boolean): コントロールのバックグラウンドをクリア/リセットします。バックグラウンドは、trueを渡すと一切描画されず、falseを渡すと描画されます。このフラグの状態は、このコントロールの子に継承されます。

    -----------------------------------------

    numberOfPopupMenus (boolean): このコントロールにアタッチされるポップアップメニューの数を返します。

    -----------------------------------------

    parent (string): コントロールの親のレイアウトです。

    -----------------------------------------

    popupMenuArray (boolean): このコントロールにアタッチされる全ポップアップメニューの名前を返します。

    -----------------------------------------

    preventOverride (boolean): trueの場合、コントロールの右マウスボタンメニューを使用したコントロールアトリビュートのオーバーライドは無効になります。

    -----------------------------------------

    spotLight (name): スポットライトの名前です。

    -----------------------------------------

    statusBarMessage (string): マウスがコントロール上にある場合にステータスバーに表示する追加の文字列です。

    -----------------------------------------

    useTemplate (string): コマンドに、現在のものとは異なるコマンドテンプレートを使用するように強制します。

    -----------------------------------------

    visible (boolean): コントロールの可視の状態です。既定では、コントロールは表示されます。コントロールの実際の外見も、その親レイアウトの可視の状態によって異なることに注意してください。

    -----------------------------------------

    visibleChangeCommand (script): コントロールの可視の状態が変更されたときに実行されるコマンドです。

    -----------------------------------------

    width (int): コントロールの幅を指定します。コントロールは親のレイアウトの条件によって無効にされない限り、このサイズを保持しようとします。

    -----------------------------------------

    widthHeight ([int, int]): ポートの幅と高さを指定します。

    -----------------------------------------

    Return Value:
    None: string- 作成または修正されたポート名照会モードでは、戻り値のタイプは照会されたフラグに基づきます。
    """
    pass

    