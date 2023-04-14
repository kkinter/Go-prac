package nodeinterface

type Node interface {
	GetChilds() []Node
	GetValue() interface{} // 아무타입이나 다 되니 빈 인터페이스 사용 or any
}