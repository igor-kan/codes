; ModuleID = 'algorithms/02_c/graphs/max_flow_dinic.c'
source_filename = "algorithms/02_c/graphs/max_flow_dinic.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct.Edge = type { i32, i32, i32 }

@head = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@it = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@.str = private unnamed_addr constant [40 x i8] c"[C Dinic] FAILED: max flow %d, want 15\0A\00", align 1
@level = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@q = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@edges = internal unnamed_addr global [2000 x %struct.Edge] zeroinitializer, align 16
@str = private unnamed_addr constant [34 x i8] c"[C Dinic] Max flow verified (=15)\00", align 1

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local range(i32 0, -2147483648) i32 @dinic(i32 noundef %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = sext i32 %1 to i64
  %5 = getelementptr inbounds i32, ptr @level, i64 %4
  %6 = sext i32 %0 to i64
  %7 = getelementptr inbounds i32, ptr @level, i64 %6
  %8 = icmp sgt i32 %2, 0
  %9 = zext i32 %2 to i64
  %10 = shl nuw nsw i64 %9, 2
  br label %12

11:                                               ; preds = %61
  br label %12, !llvm.loop !9

12:                                               ; preds = %11, %3
  %13 = phi i32 [ 0, %3 ], [ %62, %11 ]
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(400) @level, i8 -1, i64 400, i1 false)
  store i32 0, ptr %7, align 4, !tbaa !5
  store i32 %0, ptr @q, align 16, !tbaa !5
  br label %18

14:                                               ; preds = %50, %18
  %15 = phi i32 [ %20, %18 ], [ %51, %50 ]
  %16 = sext i32 %15 to i64
  %17 = icmp slt i64 %21, %16
  br i1 %17, label %18, label %55, !llvm.loop !11

18:                                               ; preds = %14, %12
  %19 = phi i64 [ 0, %12 ], [ %21, %14 ]
  %20 = phi i32 [ 1, %12 ], [ %15, %14 ]
  %21 = add nuw nsw i64 %19, 1
  %22 = getelementptr inbounds nuw i32, ptr @q, i64 %19
  %23 = load i32, ptr %22, align 4, !tbaa !5
  %24 = sext i32 %23 to i64
  %25 = getelementptr inbounds i32, ptr @head, i64 %24
  %26 = load i32, ptr %25, align 4, !tbaa !5
  %27 = icmp eq i32 %26, -1
  br i1 %27, label %14, label %28

28:                                               ; preds = %18
  %29 = getelementptr inbounds i32, ptr @level, i64 %24
  br label %30

30:                                               ; preds = %50, %28
  %31 = phi i32 [ %26, %28 ], [ %53, %50 ]
  %32 = phi i32 [ %20, %28 ], [ %51, %50 ]
  %33 = sext i32 %31 to i64
  %34 = getelementptr inbounds %struct.Edge, ptr @edges, i64 %33
  %35 = load i32, ptr %34, align 4, !tbaa !12
  %36 = getelementptr inbounds nuw i8, ptr %34, i64 4
  %37 = load i32, ptr %36, align 4, !tbaa !14
  %38 = icmp sgt i32 %37, 0
  br i1 %38, label %39, label %50

39:                                               ; preds = %30
  %40 = sext i32 %35 to i64
  %41 = getelementptr inbounds i32, ptr @level, i64 %40
  %42 = load i32, ptr %41, align 4, !tbaa !5
  %43 = icmp eq i32 %42, -1
  br i1 %43, label %44, label %50

44:                                               ; preds = %39
  %45 = load i32, ptr %29, align 4, !tbaa !5
  %46 = add nsw i32 %45, 1
  store i32 %46, ptr %41, align 4, !tbaa !5
  %47 = add nsw i32 %32, 1
  %48 = sext i32 %32 to i64
  %49 = getelementptr inbounds i32, ptr @q, i64 %48
  store i32 %35, ptr %49, align 4, !tbaa !5
  br label %50

50:                                               ; preds = %44, %39, %30
  %51 = phi i32 [ %47, %44 ], [ %32, %39 ], [ %32, %30 ]
  %52 = getelementptr inbounds nuw i8, ptr %34, i64 8
  %53 = load i32, ptr %52, align 4, !tbaa !5
  %54 = icmp eq i32 %53, -1
  br i1 %54, label %14, label %30, !llvm.loop !15

55:                                               ; preds = %14
  %56 = load i32, ptr %5, align 4, !tbaa !5
  %57 = icmp eq i32 %56, -1
  br i1 %57, label %66, label %58

58:                                               ; preds = %55
  br i1 %8, label %59, label %60

59:                                               ; preds = %58
  tail call void @llvm.memcpy.p0.p0.i64(ptr nonnull align 16 @it, ptr nonnull align 16 @head, i64 %10, i1 false), !tbaa !5
  br label %60

60:                                               ; preds = %59, %58
  br label %61

61:                                               ; preds = %60, %61
  %62 = phi i32 [ %65, %61 ], [ %13, %60 ]
  %63 = tail call fastcc i32 @dfs(i32 noundef %0, i32 noundef %1, i32 noundef 2147483647)
  %64 = icmp eq i32 %63, 0
  %65 = add nuw nsw i32 %63, %62
  br i1 %64, label %11, label %61, !llvm.loop !16

66:                                               ; preds = %55
  ret i32 %13
}

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define internal fastcc range(i32 0, -2147483648) i32 @dfs(i32 noundef %0, i32 noundef %1, i32 noundef range(i32 1, -2147483648) %2) unnamed_addr #1 {
  %4 = icmp eq i32 %0, %1
  br i1 %4, label %50, label %5

5:                                                ; preds = %3
  %6 = sext i32 %0 to i64
  %7 = getelementptr inbounds i32, ptr @it, i64 %6
  %8 = load i32, ptr %7, align 4, !tbaa !5
  %9 = icmp eq i32 %8, -1
  br i1 %9, label %50, label %10

10:                                               ; preds = %5
  %11 = getelementptr inbounds i32, ptr @level, i64 %6
  br label %12

12:                                               ; preds = %10, %33
  %13 = phi i32 [ %8, %10 ], [ %37, %33 ]
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds %struct.Edge, ptr @edges, i64 %14
  %16 = load i32, ptr %15, align 4, !tbaa !12
  %17 = getelementptr inbounds nuw i8, ptr %15, i64 4
  %18 = load i32, ptr %17, align 4, !tbaa !14
  %19 = icmp sgt i32 %18, 0
  br i1 %19, label %20, label %33

20:                                               ; preds = %12
  %21 = sext i32 %16 to i64
  %22 = getelementptr inbounds i32, ptr @level, i64 %21
  %23 = load i32, ptr %22, align 4, !tbaa !5
  %24 = load i32, ptr %11, align 4, !tbaa !5
  %25 = add nsw i32 %24, 1
  %26 = icmp eq i32 %23, %25
  br i1 %26, label %27, label %33

27:                                               ; preds = %20
  %28 = tail call i32 @llvm.smin.i32(i32 %2, i32 %18)
  %29 = tail call fastcc i32 @dfs(i32 noundef %16, i32 noundef %1, i32 noundef %28)
  %30 = icmp eq i32 %29, 0
  %31 = load i32, ptr %7, align 4, !tbaa !5
  %32 = sext i32 %31 to i64
  br i1 %30, label %33, label %39

33:                                               ; preds = %27, %12, %20
  %34 = phi i64 [ %14, %20 ], [ %14, %12 ], [ %32, %27 ]
  %35 = getelementptr inbounds %struct.Edge, ptr @edges, i64 %34
  %36 = getelementptr inbounds nuw i8, ptr %35, i64 8
  %37 = load i32, ptr %36, align 4, !tbaa !17
  store i32 %37, ptr %7, align 4, !tbaa !5
  %38 = icmp eq i32 %37, -1
  br i1 %38, label %50, label %12, !llvm.loop !18

39:                                               ; preds = %27
  %40 = getelementptr inbounds %struct.Edge, ptr @edges, i64 %32
  %41 = getelementptr inbounds nuw i8, ptr %40, i64 4
  %42 = load i32, ptr %41, align 4, !tbaa !14
  %43 = sub nsw i32 %42, %29
  store i32 %43, ptr %41, align 4, !tbaa !14
  %44 = xor i32 %31, 1
  %45 = sext i32 %44 to i64
  %46 = getelementptr inbounds %struct.Edge, ptr @edges, i64 %45
  %47 = getelementptr inbounds nuw i8, ptr %46, i64 4
  %48 = load i32, ptr %47, align 4, !tbaa !14
  %49 = add nsw i32 %48, %29
  store i32 %49, ptr %47, align 4, !tbaa !14
  br label %50

50:                                               ; preds = %33, %5, %39, %3
  %51 = phi i32 [ %2, %3 ], [ %29, %39 ], [ 0, %5 ], [ 0, %33 ]
  ret i32 %51
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(384) getelementptr inbounds nuw (i8, ptr @head, i64 16), i8 -1, i64 384, i1 false)
  store <4 x i32> <i32 1, i32 10, i32 -1, i32 0>, ptr @edges, align 16, !tbaa !5
  store <4 x i32> <i32 0, i32 -1, i32 2, i32 5>, ptr getelementptr inbounds nuw (i8, ptr @edges, i64 16), align 16, !tbaa !5
  store <4 x i32> <i32 0, i32 0, i32 0, i32 -1>, ptr getelementptr inbounds nuw (i8, ptr @edges, i64 32), align 16, !tbaa !5
  store <4 x i32> <i32 2, i32 15, i32 1, i32 1>, ptr getelementptr inbounds nuw (i8, ptr @edges, i64 48), align 16, !tbaa !5
  store <4 x i32> <i32 0, i32 3, i32 3, i32 5>, ptr getelementptr inbounds nuw (i8, ptr @edges, i64 64), align 16, !tbaa !5
  store <4 x i32> <i32 4, i32 1, i32 0, i32 -1>, ptr getelementptr inbounds nuw (i8, ptr @edges, i64 80), align 16, !tbaa !5
  store <4 x i32> <i32 3, i32 10, i32 5, i32 2>, ptr getelementptr inbounds nuw (i8, ptr @edges, i64 96), align 16, !tbaa !5
  store i32 0, ptr getelementptr inbounds nuw (i8, ptr @edges, i64 112), align 16, !tbaa !14
  store i32 7, ptr getelementptr inbounds nuw (i8, ptr @edges, i64 116), align 4, !tbaa !17
  store <4 x i32> <i32 2, i32 6, i32 8, i32 9>, ptr @head, align 16, !tbaa !5
  br label %2

1:                                                ; preds = %49
  br label %2, !llvm.loop !9

2:                                                ; preds = %1, %0
  %3 = phi i32 [ 0, %0 ], [ %50, %1 ]
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(400) @level, i8 -1, i64 400, i1 false)
  store i32 0, ptr @level, align 16, !tbaa !5
  store i32 0, ptr @q, align 16, !tbaa !5
  br label %8

4:                                                ; preds = %40, %8
  %5 = phi i32 [ %10, %8 ], [ %41, %40 ]
  %6 = sext i32 %5 to i64
  %7 = icmp slt i64 %11, %6
  br i1 %7, label %8, label %45, !llvm.loop !11

8:                                                ; preds = %4, %2
  %9 = phi i64 [ 0, %2 ], [ %11, %4 ]
  %10 = phi i32 [ 1, %2 ], [ %5, %4 ]
  %11 = add nuw nsw i64 %9, 1
  %12 = getelementptr inbounds nuw i32, ptr @q, i64 %9
  %13 = load i32, ptr %12, align 4, !tbaa !5
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds i32, ptr @head, i64 %14
  %16 = load i32, ptr %15, align 4, !tbaa !5
  %17 = icmp eq i32 %16, -1
  br i1 %17, label %4, label %18

18:                                               ; preds = %8
  %19 = getelementptr inbounds i32, ptr @level, i64 %14
  br label %20

20:                                               ; preds = %40, %18
  %21 = phi i32 [ %16, %18 ], [ %43, %40 ]
  %22 = phi i32 [ %10, %18 ], [ %41, %40 ]
  %23 = sext i32 %21 to i64
  %24 = getelementptr inbounds %struct.Edge, ptr @edges, i64 %23
  %25 = load i32, ptr %24, align 4, !tbaa !12
  %26 = getelementptr inbounds nuw i8, ptr %24, i64 4
  %27 = load i32, ptr %26, align 4, !tbaa !14
  %28 = icmp sgt i32 %27, 0
  br i1 %28, label %29, label %40

29:                                               ; preds = %20
  %30 = sext i32 %25 to i64
  %31 = getelementptr inbounds i32, ptr @level, i64 %30
  %32 = load i32, ptr %31, align 4, !tbaa !5
  %33 = icmp eq i32 %32, -1
  br i1 %33, label %34, label %40

34:                                               ; preds = %29
  %35 = load i32, ptr %19, align 4, !tbaa !5
  %36 = add nsw i32 %35, 1
  store i32 %36, ptr %31, align 4, !tbaa !5
  %37 = add nsw i32 %22, 1
  %38 = sext i32 %22 to i64
  %39 = getelementptr inbounds i32, ptr @q, i64 %38
  store i32 %25, ptr %39, align 4, !tbaa !5
  br label %40

40:                                               ; preds = %34, %29, %20
  %41 = phi i32 [ %37, %34 ], [ %22, %29 ], [ %22, %20 ]
  %42 = getelementptr inbounds nuw i8, ptr %24, i64 8
  %43 = load i32, ptr %42, align 4, !tbaa !5
  %44 = icmp eq i32 %43, -1
  br i1 %44, label %4, label %20, !llvm.loop !15

45:                                               ; preds = %4
  %46 = load i32, ptr getelementptr inbounds nuw (i8, ptr @level, i64 12), align 4, !tbaa !5
  %47 = icmp eq i32 %46, -1
  br i1 %47, label %54, label %48

48:                                               ; preds = %45
  tail call void @llvm.memcpy.p0.p0.i64(ptr noundef nonnull align 16 dereferenceable(16) @it, ptr noundef nonnull align 16 dereferenceable(16) @head, i64 16, i1 false), !tbaa !5
  br label %49

49:                                               ; preds = %49, %48
  %50 = phi i32 [ %53, %49 ], [ %3, %48 ]
  %51 = tail call fastcc i32 @dfs(i32 noundef 0, i32 noundef 3, i32 noundef 2147483647)
  %52 = icmp eq i32 %51, 0
  %53 = add nuw nsw i32 %51, %50
  br i1 %52, label %1, label %49, !llvm.loop !16

54:                                               ; preds = %45
  %55 = icmp eq i32 %3, 15
  br i1 %55, label %58, label %56

56:                                               ; preds = %54
  %57 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %3)
  br label %60

58:                                               ; preds = %54
  %59 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  br label %60

60:                                               ; preds = %58, %56
  %61 = phi i32 [ 1, %56 ], [ 0, %58 ]
  ret i32 %61
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #3

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #4

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #5

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smin.i32(i32, i32) #6

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias writeonly captures(none), ptr noalias readonly captures(none), i64, i1 immarg) #7

attributes #0 = { nofree nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree nosync nounwind sspstrong memory(readwrite, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #4 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { nofree nounwind }
attributes #6 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #7 = { nocallback nofree nounwind willreturn memory(argmem: readwrite) }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
!12 = !{!13, !6, i64 0}
!13 = !{!"", !6, i64 0, !6, i64 4, !6, i64 8}
!14 = !{!13, !6, i64 4}
!15 = distinct !{!15, !10}
!16 = distinct !{!16, !10}
!17 = !{!13, !6, i64 8}
!18 = distinct !{!18, !10}
